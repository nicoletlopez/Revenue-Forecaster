def add(x):
    if x == 1:
        return x
    else:
        return x + add(x-1)
print(add(3))
