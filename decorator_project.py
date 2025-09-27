def MyDec(func):
    def wrapper(*args, **kwargs):
        print("Before calling the function.")
        result = func(*args, **kwargs)
        print("After calling the function.")
        return result
    return wrapper
@MyDec
def say_hello(name):
    print(f"Hello, {name}!")
say_hello(input("Enter your name: "))
