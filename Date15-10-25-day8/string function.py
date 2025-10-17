#1,
text=input("enter the string :")
print("the length of the string is , len (text)")
print()

#2,
text=input("enter the string :")
print("uppercase of the string is :",text.upper())
print()

#3,
text=input("enter the string :")
print("lowercase of the string is :",text.lower())
print()

#4,
sen=input("enter the sentence :")
c=sen.count("the")
print("the","occurs",c,"times")

#5,
string=input("enter the string :")
if string.startswith("1,A"):
    print("the given string start  with A")
else:
    print("the given string is not start from A")

#6,
s=input("enter the string :")
        
if s.endswith("ing"):
         print("the given string is end eith ing")
else:
    print("the given string is not ends with ing")
print()

#7,
n=input("enter the string :")
print(n.replace(" ","-"))
print()

#8,
name=input("enter the string :")
print("index of fist a :",name.index('a'))
print()

#9,
st=input("enter the string :")
if st.isalpha():
    print("alphabet")
else:
    print("not")

#10,
n=input("enter the string :")
reverse=""
for char in n:
    reverse=char+reverse
print(reverse)
print()

         




















