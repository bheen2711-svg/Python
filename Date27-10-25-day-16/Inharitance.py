#1,
class personal:
    def name(self):
        return "barath"
    def email(self):
        print("bheen2711@gmail.com")
    def mobile(self):
        print("7708238868")
    def address(self):
        print("kariapatti")
class educational(personal):
    def bsc(self):
        print("Bsc Computer Science")
a=educational();
a.email()
print()

#2,
class personal:
    def name(self):
        print("barath")
    def email(self):
        print("bheen2711@gmail.com")
    def mobile(self):
        print("7708238868")
    def address(self):
        print("kariapatti")
class educational(personal):
    def bsc(self):
        print("Bsc Computer Science")
class bank(educational):
    def account(self):
        print("HDFC Bank")
    def no(self):
        print("2368339273")
        
a=bank()
a.name()
a.email()
a.address()
a.account()
a.no()
print()

#3,
class school:
    def name1(self):
        print("nader school")
    def email1(self):
        print("naderschoolgmail.com")
    def mobile1(self):
        print("7708238868")
    def address1(self):
        print("kariapatti")
class staff(school):
    def name2(self):
        print("jenni tamil teacher for 6 to 10")
    def mail2(self):
        print("jeni@gmail.com")
    def mobile2(self):
        print("95875878488")
    def address2(self):
        print("kariapatti")
    def dep2(self):
        print("Tamil Teacher")
class student(school):
    def name3(self):
        print("barath")
    def Class3(self):
        print("10th class A")
a=student()
b=staff()
a.name3()
a.mobile1()

