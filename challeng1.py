class book:
    def __init__(self,name,ingrediant,time,instruction):
        self.name=name
        self.ingrediant=ingrediant
        self.time=time
        self.instruction=instruction
    def display(self):
        print(self.name)
        print(self.ingrediant)
        print(self.time)
        print(self.instruction)
def wasa():
    name=input("Enter recipe name:  ")
    ingrediant=input("Enter ingrediant (comma-separated):  ")
    time=input("Enter cooking time:  ")
    instruction=input("Enter cooking instruction:  ")
    print("Recipe added sucssifolly:  ")
    return book(name,ingrediant,time,instruction)
cooking1=wasa()
print("dispaying Recipe...")
print(f"name:{cooking1.name}.")
print(f"ingrediant:{cooking1.ingrediant}.")
print(f"Time:{cooking1.time} minutes.")
print(f"instructions:{cooking1.instruction}.")
print("--------------------------------------------")
