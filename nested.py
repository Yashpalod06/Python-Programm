for i in range(10,10001):
    num=i
    digit=0
    while(num>0):
        num//=10
        digit+=1
    t2=i
    sum=0
    
    while(t2>0):
        rem=t2%10
        sum += rem ** digit
        t2//=10

    if(sum==i):
         print(i)