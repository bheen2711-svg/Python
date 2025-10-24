s=0
count=0
for i in range(100,201):
    if i%9==0:
        count+=1
        s+=i
print("nuber of integer divisible by 9:",count)
print("sum of integer divisible by 9:",s)
