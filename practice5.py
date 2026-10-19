numbers = [1, 2, 3]

it = iter(numbers)

print(next(it))  
print(next(it))  
print(next(it))  
for num in [1, 2, 3]:
    print(num)

class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        num = self.start
        self.start -= 1
        return num

cd = CountDown(5)

for i in cd:
    print(i)
def simple_gen():
    yield 1
    yield 2
    yield 3

gen = simple_gen()
print(next(gen))  
print(next(gen))  
print(next(gen))  
def squares(n):
    for i in range(n):
        yield i * i

for val in squares(5):
    print(val)

gen_exp = (x*x for x in range(5))
print(next(gen_exp))  # 0
print(next(gen_exp))  # 1
print(list(gen_exp))  # [4, 9, 16]

def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1

gen = infinite_numbers()
for i in range(5):
    print(next(gen))
