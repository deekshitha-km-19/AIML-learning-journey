x = int(input("first value:"))
y = int(input("second value:"))
x, y = y, x
print("value of x:",x)
print("value of y:",y)


str=input("enter the temperature in celsius:")
str=float(str)
print(type(str))
fahrenheittemp=(str*(9/5))+32
print("enter the temperature in fahrenheit temp:",fahrenheittemp)

radius=int(input("enter the value of radius:"))
r = radius
pi=3.14
area=pi*r**2
print("the area is:",area)