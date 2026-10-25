age = 21
if age >= 18:
    print("you can vote")
    print("you can drive")
else:
    print("you cannot vote")

age = int(input("enter your age:"))
if age >= 18:
    print("you can drive")
    print("you can vote")
else:
    print("you cannot vote")

colour = input("enter colour:")
if colour == "red":
    print("stop")
elif colour == "green":
    print("go")
elif colour == "yellow":
    print("look")
else:
    print("wrong colour for traffic lights")

age = int(input("enter your age:"))
if age < 13:
    print("child")
elif age >= 13 and age < 18:
    print("teenager")
else:
    print("adult")

username = input("enter username:")
password = input("enter password:")
if username == "admin" and password == "pass":
    print("LOGIN successful")
elif username != "admin":
    print("wrong username")
else:
    print("wrong password")

n = int(input("enter num"))
if n % 5 == 0:
    print("multiple of 5")
else:
    print("not multiple of 5")
