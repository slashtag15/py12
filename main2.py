wor=input("enter a word:")
cra=input("enter a chracter to serch:")
cnt=0
va=0
while va<len(wor):
    if wor[va]==cra:
        cnt=cnt+1
    va=va+1
print(cnt)