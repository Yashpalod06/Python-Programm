# def factoial():
#     n=int(input("enter the number"))
#     factorail=1
#     for i in range(1,n+1):
#         factorail=factorail*i
#     print(factorail) 
# fac=lambda x:x+x+x
# print(fac(3))
# c=lambda a,b,d:a+b+d
# print(c(5,10,15))
# def cube(x):
#     return x*x*x
# t=(1,2,3,40)
# tnew=tuple(map(lambda x:x*x*x,t))
# print(tnew)
# l=[1,2,3,4]
# def funct(x):
#    return x > 3
# nww=list(filter(funct,l))
# print(nww)
# from functools import reduce
# l=[1,2,3,4]
# sum=reduce(lambda x,y:x+y,l)
# print(sum)
import random

def player(a,n):
    if n==a:
     return 0 
    elif (n==0 and a==1) or  (n==1 and a==2) or (n==0 and a==2) :
     return 1
    else:
      return 2
a=random.randint(0,2)
n=int(input( "0 for Snake,1 for water,2 for Gun "))      
c= player(a,n)
print("you : ",n)
print("comp : ",a)
if (c==0):
  print("draw")
elif (c==1):
  print("win")
else:
  print("player loose")    
