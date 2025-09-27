from ursina import *
import random
import math

# ========= Tomato War - Ursina =========
WINDOW_TITLE = 'Tomato War - Prototype'
WORLD_SIZE = 80
TILE_SIZE = 2
NUM_NPCS = 10

app = Ursina()
window.title = WINDOW_TITLE
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

# -------- helper functions --------
def clamp(v, a, b):
    return max(a, min(b, v))

def floating_text(txt, position=(0,0,0), duration=1.0, color=color.white):
    t = Text(text=txt, world_position=position, origin=(0,0), background=True, color=color)
    invoke(t.fade_out, duration)
    invoke(destroy, t, delay=duration+0.1)

# -------- Ground + world (avoid void) --------
class Ground:
    def __init__(self, world_size=WORLD_SIZE, tile_size=TILE_SIZE):
        self.world_size = world_size
        self.tile_size = tile_size
        self.tiles_parent = Entity()
        self._make_tiles()
        self._make_boundaries()

    def _make_tiles(self):
        half = int(self.world_size/2)
        for x in range(-half, half):
            for z in range(-half, half):
                Entity(parent=self.tiles_parent, model='plane', collider='box',
                       scale=self.tile_size, position=(x*self.tile_size, 0, z*self.tile_size),
                       rotation_x=90,
                       color=color.lime.tint(random.uniform(-0.15, 0.05)))
        # decorative cubes
        for i in range(int(self.world_size*1.5)):
            rx = random.uniform(-half*self.tile_size, half*self.tile_size)
            rz = random.uniform(-half*self.tile_size, half*self.tile_size)
            Entity(model='cube', scale=(random.uniform(0.7,2), random.uniform(0.7,2), random.uniform(0.7,2)),
                   position=(rx, 0.5, rz), color=color.rgb(100,100,100).tint(random.uniform(-0.1,0.2)))

    def _make_boundaries(self):
        half_world = self.world_size/2 * TILE_SIZE
        wall_thickness = 1
        wall_height = 5
        # walls
        Entity(model='cube', scale=(wall_thickness, wall_height, WORLD_SIZE*TILE_SIZE),
               position=(half_world + wall_thickness/2, wall_height/2, 0), color=color.gray, collider='box')
        Entity(model='cube', scale=(wall_thickness, wall_height, WORLD_SIZE*TILE_SIZE),
               position=(-half_world - wall_thickness/2, wall_height/2, 0), color=color.gray, collider='box')
        Entity(model='cube', scale=(WORLD_SIZE*TILE_SIZE, wall_height, wall_thickness),
               position=(0, wall_height/2, half_world + wall_thickness/2), color=color.gray, collider='box')
        Entity(model='cube', scale=(WORLD_SIZE*TILE_SIZE, wall_height, wall_thickness),
               position=(0, wall_height/2, -half_world - wall_thickness/2), color=color.gray, collider='box')

# -------- Player --------
class Player(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.body = Entity(parent=self, model='cube', scale=(1,1.4,1), color=color.azure)
        self.head = Entity(parent=self, model='sphere', position=(0,0.9,0), scale=0.6, color=color.rgb(255,224,189))
        self.collider = 'box'
        self.level, self.xp, self.xp_to_next = 1, 0, 50
        self.max_hp, self.hp = 100, 100
        self.damage, self.speed, self.jump_power = 18, 6, 6
        self.velocity = Vec3(0,0,0)
        self.grounded = False
        self.throw_cooldown, self.throw_timer = 0.6, 0
        for k,v in kwargs.items():
            setattr(self, k, v)

    def give_xp(self, amount):
        self.xp += amount
        if self.xp >= self.xp_to_next:
            self.xp -= self.xp_to_next
            self.level_up()

    def level_up(self):
        self.level +=1
        self.max_hp +=20
        self.hp = self.max_hp
        self.damage = int(self.damage*1.12)
        self.speed +=0.4
        self.jump_power +=0.4
        self.xp_to_next = int(self.xp_to_next*1.5)
        floating_text(f"Level up! {self.level}", position=self.position+Vec3(0,2,0), color=color.gold)

    def throw_tomato(self):
        if self.throw_timer>0: return
        dir = camera.forward
        pos = self.world_position + Vec3(0,1.0,0) + dir*1.4
        TomatoProjectile(position=pos, direction=dir, owner=self, damage=self.damage)
        self.throw_timer = self.throw_cooldown

    def update(self):
        dt = time.dt
        if self.throw_timer>0: self.throw_timer -= dt
        forward, back = held_keys['w'] or held_keys['up arrow'], held_keys['s'] or held_keys['down arrow']
        left, right = held_keys['a'] or held_keys['left arrow'], held_keys['d'] or held_keys['right arrow']
        move_dir = Vec3(0,0,0)
        cam_fwd = Vec3(camera.forward.x,0,camera.forward.z).normalized()
        cam_right = Vec3(camera.right.x,0,camera.right.z).normalized()
        if forward: move_dir+=cam_fwd
        if back: move_dir-=cam_fwd
        if right: move_dir+=cam_right
        if left: move_dir-=cam_right
        move_dir = move_dir.normalized() if move_dir.length()>0 else Vec3(0,0,0)
        self.position += move_dir*self.speed*dt
        # gravity
        self.velocity.y -= 9.8*dt
        ray = raycast(self.world_position+Vec3(0,0.6,0), Vec3(0,-1,0), distance=1.2, ignore=(self,))
        if ray.hit:
            self.grounded = True
            self.position = Vec3(self.position.x, ray.world_point.y+0.01, self.position.z)
            self.velocity.y = 0
        else:
            self.grounded=False
            self.position += self.velocity*dt
        if move_dir.length()>0.1:
            target_angle = math.degrees(math.atan2(move_dir.x, move_dir.z))
            self.rotation_y = lerp(self.rotation_y, target_angle, 6*dt)

    def input(self, key):
        if key=='space' and self.grounded:
            self.velocity.y = self.jump_power
            self.grounded=False
        if key=='left mouse down' or key=='right mouse down':
            self.throw_tomato()

# -------- Tomato Projectile --------
class TomatoProjectile(Entity):
    def __init__(self, position=(0,0,0), direction=Vec3(0,0,1), owner=None, damage=10):
        super().__init__()
        self.model='sphere'
        self.scale=0.45
        self.color=color.rgb(220,40,60)
        self.position = position
        self.collider='sphere'
        self.direction = direction.normalized()
        self.speed = 18
        self.owner = owner
        self.damage = damage
        self.life_time=4

    def update(self):
        dt = time.dt
        self.position += self.direction*self.speed*dt
        self.life_time -= dt
        hit = self.intersects()
        if hit.hit:
            ent = hit.entity
            if ent and ent is not self.owner and hasattr(ent,'on_hit'):
                ent.on_hit(self.damage,self.owner)
                for i in range(6):
                    Entity(model='cube', scale=0.1, position=self.position + Vec3(random.uniform(-0.2,0.2),
                           random.uniform(-0.2,0.2), random.uniform(-0.2,0.2)), color=color.rgb(200,30,40), lifetime=1)
                destroy(self)
                return
        if self.life_time<=0: destroy(self)

# -------- NPC --------
class NPC(Entity):
    def __init__(self, position=(0,0,0), **kwargs):
        super().__init__()
        self.body = Entity(parent=self, model='cube', scale=(0.9,1.2,0.9), color=color.orange)
        self.head = Entity(parent=self, model='sphere', position=(0,0.9,0), scale=0.6, color=color.rgb(255,224,189))
        self.collider='box'
        self.health,self.max_health = 60,60
        self.damage = 10
        self.speed = random.uniform(2.2,3.4)
        self.aggro_range = 12
        self.throw_cooldown = random.uniform(1.0,2.0)
        self.throw_timer = random.uniform(0,self.throw_cooldown)
        self.state='idle'
        self.wander_target = None
        self.target=None
        self.position = position
        for k,v in kwargs.items(): setattr(self,k,v)

    def on_hit(self, damage, attacker):
        self.health -= damage
        floating_text(str(damage), position=self.position+Vec3(0,1.7,0), duration=0.6, color=color.red)
        self.target = attacker
        self.state = 'chase'
        if self.health <= 0: self.die()

    def die(self):
        if self.target and hasattr(self.target,'give_xp'):
            self.target.give_xp(20)
        for i in range(8):
            Entity(model='sphere', scale=0.12, position=self.position + Vec3(random.uniform(-0.6,0.6),
                   random.uniform(0,1.2), random.uniform(-0.6,0.6)), color=color.rgb(200,30,40), lifetime=1.2)
        destroy(self)

    def update(self):
        dt = time.dt
        player_ent = player
        if not player_ent: return
        dist = distance(self.position, player_ent.position)
        if dist<self.aggro_range or self.target:
            self.state='chase'
            self.target=player_ent
        else:
            if self.state!='wander' or (self.wander_target and distance(self.position,self.wander_target)<1):
                self.state='wander'
                x=random.uniform(-WORLD_SIZE/2*TILE_SIZE, WORLD_SIZE/2*TILE_SIZE)
                z=random.uniform(-WORLD_SIZE/2*TILE_SIZE, WORLD_SIZE/2*TILE_SIZE)
                self.wander_target = Vec3(x,0,z)
        if self.state=='wander' and self.wander_target:
            dir = (Vec3(self.wander_target.x,0,self.wander_target.z)-Vec3(self.position.x,0,self.position.z)).normalized()
            self.position += dir*self.speed*dt
            target_angle = math.degrees(math.atan2(dir.x, dir.z))
            self.rotation_y = lerp(self.rotation_y, target_angle, 3*dt)
        elif self.state=='chase' and self.target:
            dir = (Vec3(self.target.position.x,0,self.target.position.z)-Vec3(self.position.x,0,self.position.z))
            dlen = dir.length()
            dir = dir.normalized() if dlen>0 else Vec3(0,0,0)
            if dlen>6: self.position += dir*self.speed*dt
            target_angle = math.degrees(math.atan2(dir.x, dir.z))
            self.rotation_y = lerp(self.rotation_y, target_angle, 6*dt)
            if self.throw_timer<=0 and dlen<14:
                aim = (self.target.position - self.position + Vec3(random.uniform(-1,1), random.uniform(0.2,1.0), random.uniform(-1,1))).normalized()
                TomatoProjectile(position=self.position+Vec3(0,1.0,0)+aim*1.2, direction=aim, owner=self, damage=self.damage)
                self.throw_timer = self.throw_cooldown
        if self.throw_timer>0: self.throw_timer -= dt

# -------- HUD --------
class HUD(Entity):
    def __init__(self):
        super().__init__()
        self.hp_bar = Entity(parent=camera.ui, model='quad', scale=(0.35,0.04), position=Vec2(-0.7,0.4), color=color.red)
        self.hp_text = Text(parent=camera.ui, text='', position=Vec2(-0.7,0.46), scale=1.6)
        self.xp_text = Text(parent=camera.ui, text='', position=Vec2(-0.7,0.35), scale=1.3)
        self.level_text = Text(parent=camera.ui, text='', position=Vec2(-0.7,0.31), scale=1.5)
        self.msg = Text(parent=camera.ui, text='Tomato War - Left click to throw', position=Vec2(0,0.45), origin=(0,0), scale=1.1)
    def update(self):
        hp_ratio = player.hp/player.max_hp if player and player.max_hp>0 else 0
        self.hp_bar.scale_x = 0.35*clamp(hp_ratio,0,1)
        self.hp_text.text = f'HP: {int(player.hp)}/{int(player.max_hp)}'
        self.xp_text.text = f'XP: {player.xp}/{player.xp_to_next}'
        self.level_text.text = f'Lvl: {player.level}'

# -------- Tomato Pickup --------
class TomatoPickup(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene, model='sphere', scale=0.4, color=color.rgb(220,40,60), position=position)
        self.collider='sphere'
    def on_click(self):
        player.hp = min(player.max_hp, player.hp+12)
        player.give_xp(8)
        floating_text('+heal', position=self.position+Vec3(0,1,0))
        destroy(self)

# -------- create world, player, NPCs --------
ground = Ground()
player = Player(position=(0,1,0))
camera.parent = player
camera.position = Vec3(0,6,-12)
camera.rotation_x = 14
mouse.locked = False

npcs = []
for i in range(NUM_NPCS):
    x=random.uniform(-WORLD_SIZE/2*TILE_SIZE, WORLD_SIZE/2*TILE_SIZE)
    z=random.uniform(-WORLD_SIZE/2*TILE_SIZE, WORLD_SIZE/2*TILE_SIZE)
    npcs.append(NPC(position=(x,0,z)))

hud = HUD()
cross = Entity(parent=camera.ui, model='quad', scale=0.01, position=(0,0), color=color.white)

for i in range(int(WORLD_SIZE/4)):
    x=random.uniform(-WORLD_SIZE/2*TILE_SIZE, WORLD_SIZE/2*TILE_SIZE)
    z=random.uniform(-WORLD_SIZE/2*TILE_SIZE, WORLD_SIZE/2*TILE_SIZE)
    TomatoPickup(position=(x,0.4,z))

# -------- update --------
def update():
    hud.update()
    cam_target = player.position + Vec3(0,6,-12)
    camera.world_position = lerp(camera.world_position, cam_target, 6*time.dt)
    camera.look_at(player.position+Vec3(0,1.6,0))
    half_world = WORLD_SIZE/2*TILE_SIZE
    player.position = Vec3(clamp(player.position.x,-half_world+1,half_world-1),
                           player.position.y,
                           clamp(player.position.z,-half_world+1,half_world-1))

def input(key):
    if key=='r':
        player.position=Vec3(0,2,0)
        player.hp=player.max_hp
    if key=='tab': mouse.locked = not mouse.locked

if __name__=='__main__':
    app.run()
