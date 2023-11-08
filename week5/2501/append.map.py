# append.map.py

arr = ["1", "2"]

a, b = map(int, arr)  # a=1, b=2
print("map")
print(a, b)
for i in map(int, arr):
    print(i)

print()

c, d = range(2)  # c=0,d=1
print("range")
print(c, d)
for i in range(2):
    print(i)
