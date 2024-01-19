# x="python"
# y=""
# last=len(x)-1

# for i in range(last,-1,-1):
#     y+=x[i]

# if(x==y):
#     print("p")
# else:
#     print("Not P")    
##65-90 uppercase(A-Z)
##97-122 lower case(a-z)
##ord-odinal
x="pyThOn"

for i in x:
    if(ord(i)>96 and ord(i)<123):
        print(chr((ord(i)-32)),end="")
    elif(ord(i)>64 and ord(i)<91):
        print(chr((ord(i)+32)),end="")
    elif(ord(i)==32):
        print()
