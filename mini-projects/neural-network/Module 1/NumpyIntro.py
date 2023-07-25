import numpy as np

a = np.array([[1,2,3],[4,5,6]], dtype=float)
print(a.shape)
print(a.dtype)
print(f"List: {a}")
print('---')
print(a[0,0])

print('\n----ZEROS--------')
b = np.zeros((3,4))
print("shape:", b.shape)
print("printing:", b)

print('\n---FULL---------')
c = np.full((3,4), 2)
print("shape:", c.shape)
print("printing:", c)

print('\n----SHAPE--------')
d = np.arange(3, 30, 3)
print("shape:", d.shape)
print("printing:", d)

print('\n--RESHAPE----')
e = np.arange(40)
e = e.reshape((4,10))
print("shape:", e.shape)
print("printing:", e)

print('\n--RANDOM FLOAT NUMBERS----')
f = np.random.random((4,4))
print("Random:", f)

print('\n--RANDOM INT NUMBERS----')
g = np.random.randint(0,100,(4,5))
print("Random:", g)

print('\n--AXIS----')
h = np.array([[1,2,3],[4,5,6]])
# sum colums
i = h.sum(axis=0)
print("sum colums: ", i)
# sum rows
j = h.sum(axis=1)
print("sum rows: ", j)
