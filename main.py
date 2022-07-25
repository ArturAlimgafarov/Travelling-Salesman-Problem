import random

l = [random.randint(0, 100) for _ in range(10)]
print(l)

def f(a):
    i, j = random.randint(0, 10), random.randint(0, 10)
    a[i], a[j] = a[j], a[i]

f(l)
print(l)