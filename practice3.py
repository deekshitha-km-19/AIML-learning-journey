def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(age=25, name="deeee")
def total_sum(*numbers):
    result = 0
    for num in numbers:
        result += num
    return result

print(total_sum(1, 2, 3, 4))
def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="chintu", age=19, course="Python")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
def outer_function(name):
    def inner_function():
        print(f"Hello, {name}!")
    inner_function()

outer_function("deeksha")