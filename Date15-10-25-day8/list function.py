'''#1,
l=[]
number=int(input("enter the number :"))
for i in range(number):
    num=input("enter the value :")
    l.append(num)
print(l)
print()

#2,
fruites=["apple","crange","grapes","pineapple","mango"]
for i in fruites:
    print(i)
print()

#3,
name=[]
for i in range(3):
    n=input("enter the name")
    name.append(n)

    if n=='stop':
        break
    print(name)
print()

#4,
l=[1,5,7]
for i in range(2,10):
    l.append(i)
print(l)
print()

#5,
city=["madurai","chennai","erode"]
print(city)
city.remove("madurai")
print("remove one  city",city)
print()

#6,
n=[]
element=int(input("enter the element"))
for i in range(element):
    v=input("enter the value")
    n.append(v)
print(n)
n.pop(-1)
print("remove the last element using pop\n",n)

#7,
sub=[]
for i in range(5):
    s=input("enter the subject")
    sub.append(s)
print(sub)
print()

#8,
l=["tamil","english","max","scince","social"]
print(l)
r=input("enter you want to remove a specific item")
l.remove(r)
print(l)
print()

#9,
num=[]
for i in range(1,11):
    num.append(i)
print(num)
print()'''

#10,
num=[1,2,3,4,5,6,7,8,9]
odd=[]
print(num)
for i in range(num):
    if i%2!=0:
        odd.append(i)
print("remove even number:",odd)
