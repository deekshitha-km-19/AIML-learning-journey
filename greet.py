def function_name(parameters):
    
 def greet():
    print("Hello! Welcome to the Python course.")
 greet()

def greet_user(name):
    print(f"Hello, {name}! Welcome to the Python course.")

greet_user("deeksha")
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 20)
print("The sum is:", result)

def greet(name="Student"):
    print(f"Hello, {name}! Welcome to the Python course.")

greet()  
greet("deeksha")  
name = "Global Name"

def greet():
    name = "Local Name"
    print(name)

greet()  # Prints local variable
print(name)  # Prints global variable
