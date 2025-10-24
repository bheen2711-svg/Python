#1,
d={}
num=int(input("enter the count"))
for i in range(num):
        key=input("enter the key :")
        value=input("enter the value :")
        d[key]=val
print("dictiory :",d)
key=input("enter the key value")
if key in d:
        print("given key is exist")
else:
    print("given key is not exist")
print()

#2,
d={}
num=int(input("enter the count :"))
for i in range(num):
    key=input("enter the key :")
    val=input("enter the value:")
    d[key]=val
print("dictiory :",d)
for key, val in d.item():
    print(key,d[key])
print()
#3,
d={}
num=int(input("enter the count :"))
for i in range(num):
    key=int(input("enter the key :"))
    val=key**2
    d[key]=val
print("dictory :",d)
print()

#4,
a={23:"leo",4:"batath",58:100,22:"sanji"}
for key,value in a.items():
    print(f"Key:{key},Value:{value}")
print()

#5,
a={x:x**2 for x in range(1,10)}
print(a)
print()

#6,
a={23:"leo",4:"barath",20:30,22:"barth"}
s.pop(4)
print(a)
print()

#7,
a={23:"leo",4:"batath",58:100,22:"sanji"}
b=len(a)
print("the length of the dict is:",b)
print()

#8,
a={23:"leo",4:"batath",58:100,22:"sanji"}
a.setdefault(2,"nill")
print(a)
print()

#9,
d=()
num=int(input("enter a count:" ))
for i in range(num):
    key=input("enter the key value:")
    va.keys()
print()

#10,
d=()
num=int(input("enter a count:"))
for i in range(num):
    key=input("enter the key value:")
    val=input("enter the value:")
    d[key]=val
print("dictinory :",d)
print(type(key))
