def get_largest (a, b, c): 
	if a > b and a > c:
		return a
	elif b > c:
		return b
	else:
		return c
print (get_largest (3, 10, 5))
n = int(input("enter n: ")) 
fact = 1 
for i in range (1, n+1): 
	fact *= i
print("factorial = ", fact)

word = input("enter a word: ")
count = 0
for ch in word:
 if (ch == 'a' or ch == 'a' or ch == 'a' or ch == 'a' or ch == 'a'):
  count += 1
print(f"vowel count = {count}")

n = int(input("enter n: "))
sum = 0
for i in range(1, n+1):
 sum += i
print("sum = ", sum)