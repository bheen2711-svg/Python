n=int(input("enter the number:"))
total=0
for i in range(1,n+1):
    term=1/i
    print("1/",i,"+",end='')
    total+=term

print('\n'"the sum of hormoic series:",total)
