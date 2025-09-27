import pygame
import random

# ---------------- إعداد اللعبة ----------------
pygame.init()
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect the Coins!")

# الألوان
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
YELLOW = (255, 255, 0)

# ---------------- إعداد اللاعب ----------------
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# ---------------- إعداد النقاط ----------------
coin_size = 30
coin_x = random.randint(0, WIDTH - coin_size)
coin_y = random.randint(0, HEIGHT - coin_size)

score = 0
font = pygame.font.SysFont(None, 36)

# ---------------- حلقة اللعبة ----------------
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # FPS

    # -------- أحداث اللعبة --------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------- تحريك اللاعب --------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x - player_speed >= 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed + player_size <= WIDTH:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y - player_speed >= 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y + player_speed + player_size <= HEIGHT:
        player_y += player_speed

    # -------- الاصطدام مع النقاط --------
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    coin_rect = pygame.Rect(coin_x, coin_y, coin_size, coin_size)
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_x = random.randint(0, WIDTH - coin_size)
        coin_y = random.randint(0, HEIGHT - coin_size)

    # -------- رسم العناصر --------
    win.fill(BLACK)
    pygame.draw.rect(win, RED, player_rect)
    pygame.draw.rect(win, YELLOW, coin_rect)
    score_text = font.render(f"Score: {score}", True, WHITE)
    win.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
