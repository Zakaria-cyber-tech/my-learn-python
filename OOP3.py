class user:
    def __init__(self,first_name,last_name,email,password,status="inactive"):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.status=status
    def display(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.password)
        print(self.status)
    def acti(self):
        self.status="active"
def create():
    first=input("Enter your First Name: ")
    last=input("Enter your last name: ")
    email=input("Enter your email: ")
    password=input("Enter Your password: ")
    return user(first,last,email,password)
user1=create()
user1.acti()
user1.display()
