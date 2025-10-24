#1,
def diction(**a):
    for i,j in a.items():
        print("key",i,"value",j)
        print(a.keys())
def user_input():
    a=input("enter the number :")
    b=input("enter the number :")
    c=input("enter the number :")
    d=input("enter the number :")
    diction(a=b,b=b,c=c,d=d)
user_input()
print()

#2,
def diction(**a):
    for i,j in a.items():
        print("key",i,"value",j)
    print(a.values())
diction(a=10,b=20,c='leo',d=70)
print()

#3,
def s(*b):
    print(sum(b))
a=int(input("enter the number :"))
b=int(input("enter the number :"))
c=int(input("enter the number :"))
s(a,b,c)
print()

#4,
def even(*a):
    ev=[]
    for i in a:
        if i%2==0:
         ev.append(i)
        print("even number",ev)
even(1,2,3,4,5,6,7,8,9)

#5,
def perfect_number(*a):
    for n in a:
        sum1=0
        for i in range(1,n):
            if n%1==0:
                sum1=sum1+1
            if sum1==n:
                print(n,"is a perfect num")
            else:
                    print(n,"is not perfect num")
perfect_number(2,4,28)
print()

#6,
def remove_last(**a):
    print("before remove :",a)
    a.popitem()
    print("afer remove :",a)
remove_last(a=10,b=30,c="leo",d=60)
print()

#7,
def calculactor(a,b,op):
    if op =='+':
        print("addition is:",a+b)
    elif op =='-':
        print("subtraction is:",a-b)
    elif op =='*':
        print("multiplication  is:",a*b)
    elif op =='/':
        print("division is:",a/b)
    else:
        print("invalid operator")
calculactor(10,20,'+')
print()

#8,
def palindrom(a):
    if a ==a[::-1]:
        print(a,"is palindrom")
    else:
        print(a, "is not palindrom")
palindrom("naa the da")
palindrom("amma")
print()

#9,
def count_string(a):
    v = c = s = 0
    for ch in a:
        if ch.lower() in "aeiou":
            v = v + 1
        elif ch.isalpha():
            c = c + 1
        else:
            s = s + 1
            print("vowels:",v)
            print("consonats:",c)
            print("special characterrs :",s)

count_string("hello 124")
        
