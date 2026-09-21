print("Love") #output

father_name = input("Father Name: ")
father_age = int(input("Father Age: "))
mother_name = input("Mother Name: ")
mother_age = int(input("Mother Age: "))
daughter_name = input("Daughter Name: ")
daughter_age = int(input("Daughter Age: "))

#absolue value (abs) function
age_diff1 = abs(father_age - daughter_age)
age_diff2 =abs(mother_age - daughter_age)
#formated string
print(f"{father_name} loves daughter {daughter_name}. Age Difference is {age_diff1}")
#concatination string
print(mother_name + " loves daughter " + daughter_name + ". Age Difference is " + str(age_diff2))