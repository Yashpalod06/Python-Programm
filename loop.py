# print(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)
# i=1
# sum=0
# while(i<11):
#     if(i%2==0):
#       sum+=i
#       i+=i
#     else:
#         i+=i
# print(sum)
# range=range(start,stop,skip) parametercan be passed
# skip=n-1 times 
# sum=0
# product=1
# count=0
# for i in range(25,78):
#     sum+=i
#     product*=i
#     count=count+1
# print(sum)
# print(product)
# print(count)
# i=int(input("Enter the number :"))
# sum=0
# while(i<79):
#     if(i%2!=0):
#          sum=sum+i
#          i=i+1
#     else:
#          i=i+1     
# print(sum)    
# num=7
# for i in range(2,num):
#      if(num % i== 0):
#         print("Not prime")
#      else:
#         print("prime")
           
# num=7
# bol=False
# for i in range(2,num):
#      if(num % i== 0):
#          bol=False
#      else:
#           bol=True
# if(bol==False):
#      print("not prime")
# else:
#      print("Prime")               
        
sum=0
count=0
for i in range(13,49):
     num=i
     bol=True
     for i in range(2,num):
          if(num%i==0):
               bol=False    
     if(bol==True):
          sum+=num
          count+=1
print(sum)
print(count)

num=13
sum=0
count=0
bol=True
for i in range(2,num):
     if(num%i==0):
          bol=False
     else:     
         for i in range(num,79):
               if(num%i==0): 
                    bol=False
               if(bol==True):
                    sum+=num
                    count+=1
     print(sum)     






         


   
            