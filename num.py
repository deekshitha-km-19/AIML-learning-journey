import numpy as np
a= np.array([1,2,3,4,5])
print(a)

a = np.arange(1, 9)
print(a)

a= np.linspace(10,7,9)
print(a)

a=np.zeros((5,6))
print(a)

b=np.ones((7,9))
print(b)

c= np.reshape([8,9,4,5,6,2,4,4,4,],(3,3))
print(c)

d=np.array([6,7,5])
e=np.array([7,8,6,])
print(np.concatenate([d,e]))

a=np.sum([6,78,90])
print(np.sum(a))
b=np.mean([6,88,44])
print(np.mean(b))
c=np.min([7,9,44])
print(np.min(c))

v=np.max([5,7,8,1])
print(np.max(v))
m=np.std([6,88,9,2])
print(np.std(m))
a=np.argmax([33,66,88])
print(np.argmax(a))
d=np.argmin([99,88,66,22,76])
print(np.argmin(d))


