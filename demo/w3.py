import os

def fd(a,l=[]):
   l.append(a)
   print(hex(id(l)))
   print(l)

def fd2(a,l=None):
   if l is None:
      l=[]
   print(hex(id(l)))
   l.append(a)
   print(l)

def f_nfa(a,*args):
   print(a)
   print(len(args))
   print(args[0])
   #args[0]=1

def f_nfd(a,**argv):
   for k in argv:
      print(k,end='\t')
      print(argv[k])

def outer(x):
   
   def inner(y):
      nonlocal x
      x+=y
      return x

   return inner

def f_s(a,b,*,c):
   return a+b+c

def f_an(a:int,b:str='test')->"return b[a]":
   return b[a]

def main():

   print(f_an(1))
   #print(f_s(1,2,3))
   #print(f_s(1,2,c=3))
   #print(outer(10)(1))
   #print(outer(10)(2))
   #f1=outer(10)
   #print(f1)
   #print(f1(1))
   #print(f1(2))
   #l=[1,2,3]
   #fd(100)
   #fd(200)
   #fd(300)
   fd2(100)
   fd2(200)
   fd2(300)
   #f_nfa(1,'test',2,3,'test')
   #f_nfa(2,3,4,5,6,7,8)
   #f_nfd(1,a1=2,b1=4)

   pass

if __name__=='__main__':
   main()