total_bill = float(input("enter the total bill amount: "))
num_friends = int(input("enter number of friends to split the bill: "))
bill_per_person = total_bill / num_friends
print("each person should pay: ", bill_per_person)
print("data type of bill_per_person is:",type(bill_per_person))
