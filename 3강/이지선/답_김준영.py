a=int(input())

def fac(x):
    if x > 1:
        return x * fac(x - 1)
    else:
        return 1

print(fac(a))