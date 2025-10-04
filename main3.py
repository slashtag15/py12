sta=int(input("enter a starting index:"))
end=int(input("enter a ending index:"))
n=0
for i in range(sta,end+1):
    if i%2==0:
        n=n+i
print(n)