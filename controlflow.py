# x=int(input("Enter  number1 : "))
# y=int(input("Enter number2 : "))
# z=int(input("Enter number3 : "))
# if (x>y and x>z) :
#     print("X is greater :",x)
# elif (y>x and y>z):
#     print("Y is greater :",y)     
# else:
#     print("Z is greater :",z)    
marks=int(input("Enter Marks : "))   
if marks>80 and marks<=100 :
    print("A grade")
elif marks>65 and marks<=80 :
    print("B grade")
elif marks>45 and marks<=65:
    print("C grade")
elif marks>33 and marks<=45 :
    print("D grade")
elif marks>=0 and marks <=35:
    print("Fail") 
else:
    print("Invalid Marks")       
