for i in range(1,1000):
    sum=0
    prod=1
    num =i
    while i>0:
        sum=sum+(i%10)
        prod=prod*(i%10)
        i=i//10
    if (sum == prod):
        print(num)Ṇ