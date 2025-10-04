num=int(input("enter a number:"))
sum=0
while num>0:
    dig=num%10
    sum=dig+sum
    num=num//10
print(sum)
