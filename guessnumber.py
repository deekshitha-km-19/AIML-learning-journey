secret_number=19
guess= int (input("guess a number between 1and 20: "))
if guess==secret_number:
    print("correct! you won!")
elif guess>secret_number:
    print("too high! try a smaller number.")
else:
    print("too low! try a larger number.")  
    