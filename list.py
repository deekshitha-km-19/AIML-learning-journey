fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["apple", 3, True]

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["apple", 3, True]
print(fruits[-1])  
print(fruits[-2])  
print(numbers[-1])  
print(numbers[-2])  
print(mixed[-1])  
print(mixed[-2]) 

fruits.append("grape")
print(fruits)  

fruits.insert(1, "kiwi")
print(fruits)  

fruits.remove("banana")
print(fruits) 

fruits.pop()  
print(fruits)  

fruits.pop(0)  
print(fruits)
fruits.clear()
print(fruits)

numbers = [0, 1, 2, 3, 4, 5, 6]
print(numbers[1:4])  
print(numbers[:4])  
print(numbers[2:])  
print(numbers[::2])