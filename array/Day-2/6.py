"""

"""
low=2
high=10

for i in range(low,high+1):
    if i %2==0 or i%5==0:
        print(i)


print(list(filter(lambda x: x%2==0 or x%5==0, range(low,high+1))))