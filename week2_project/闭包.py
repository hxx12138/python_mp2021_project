b = [0,1,2]
def outer(x):
    def inner(y):
        nonlocal x
        x+=y
        b[0]+=y
        return x
    return inner
f1 = outer(10)
print(f1(1))
print(f1(2))
print(outer(10)(1))
print(outer(10)(2))