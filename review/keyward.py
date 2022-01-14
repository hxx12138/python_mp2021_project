
# assert

assert(True)
#print('success')
#assert(False)

'''Traceback (most recent call last):
  File "/Users/xihe/Documents/python_mp2021_project/review/keyward.py", line 3, in <module>
    assert(False)
AssertionError'''


# is 判断引用对象是否为同一个

'''a = '1234'
b = '1234'
print(a is b)
print(id(a))
print(id(b))

c = [0]
d = [0]
print(c is d)
print(id(c))
print(id(d))'''


# lambda 匿名函数

'''print(lambda x: x*x*x)

f = lambda x : x*x
print(f(1))
def f(x):
    return x * x
print(f(1))

def build(x, y):
    return lambda: x * x + y * y

def is_odd(n):
    return n % 2 == 1

#L = list(filter(is_odd, range(1, 20)))

L = list(filter(lambda x : x%2==1 ,range(1,20)))
print(L)
'''


# nonlocal 闭包



# yield 迭代器和生成器

'''def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b      # 使用 yield
        # print b 
        a, b = b, a + b 
        n = n + 1
 
f = fab(5)
while True: 
    print(f.__next__())'''

'''list1=['A','B','C'] 
list2=list1 
list1.append('D') 
print(list2)'''

dt = {'k1': 1, 'k2': 2, 'k3': 3} 
print('k1: {0[k1]}; k2: {0[k2]}; k3: {0[k3]}'.format(dt))