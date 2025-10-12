n=int(input("enter the number"))
even=0
odd=0
for i in range(1,n+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
        print("even number:",even)
        print("odd number:",odd)
