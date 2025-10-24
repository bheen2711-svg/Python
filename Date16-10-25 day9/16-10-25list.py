#1,
l=[]
n=int(input("enter the number of fruites :"))
for i in range(n):
    val=input("enter the fruites :")
    l.append(val)
print(l)
print()

#2,
l=["apple","orange","mango"]
n=input("enter the new fruit you want :")
l.append(n)
print("add one new fruites \n",l)
r=input("enter the fruites you want :")
confirm=int(input("are you sure if yes 1 or else press 2 :"))
if confirm==1:
    l.remove(r)
    print(l)
else:
    print(l)
print()

#3,
a=[1,2,3,4,5]
b=max(a)
print("the max value",b)
c=min(a)
print("the min value",c)

#4,
l=[]
c=int(input("enter the number of element :"))
for i in range(c):
    val=int(input("enter the number you want:"))
    l.append(val)
print("you original list :",l)
l.sort()
print("assesending order :",l)

#5,
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

#6,
a=[]
count=int(input("enter num of cityes"))
for i in range(count):
    b=input("enter the cityes")
    a.append(b)
print(a)

#7,
a=[12,3,4,6]
sum=0
for i in a:
    s
    um+=1
print(sum)

#8,
a=[1,2,3,4,5,6,7]
count=0
for i in range(a):
    if 1%2==0:
        count+=1
print(count)
