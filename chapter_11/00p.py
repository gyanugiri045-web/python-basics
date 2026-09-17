
###  int method

class computer:
    def __init__(self, cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("config is ", self.cpu, self.ram)

com1 = computer("i5", 50)
com2 = computer("i6", 40)
com3 = computer("i6", 30)

com1.config()
com2.config()
com3.config()





### constructor , self and comparing objects

class computer:

    def __init__(self):
        self.name="ram"
        self.age=40

    def compare(self,others):
        if self.age == others.age:
            return True
        else:
            return False
        
c1= computer()
c1.age=30
c2= computer()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

print(c1.name)
print(c2.name)




### types of variables

class car:
    weel=4         ### class veriable

    def __init__(self):
        self.mil=40       ## instance veriable
        self.com="BMW"    ## instance veriable 
   
c1=car()
c2=car()

c1.mil=20
car.weel=8

print(c1.mil,c1.com,c1.weel)
print(c2.mil,c2.com, c2.weel)



## types of methods 

class student:
    school="Sundarban"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    
    @classmethod
    def info(cls):
        return cls.school
    
s1=student(45,55,67)
s2=student(22,33,44)


print(s1.avg(),s1.school)
print(s2.avg(),s2.school)



###  int method

class computer:
    def __init__(self, cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("config is ", self.cpu, self.ram)

com1 = computer("i5", 50)
com2 = computer("i6", 40)
com3 = computer("i6", 30)

com1.config()
com2.config()
com3.config()





### constructor , self and comparing objects

class computer:

    def __init__(self):
        self.name="ram"
        self.age=40

    def compare(self,others):
        if self.age == others.age:
            return True
        else:
            return False
        
c1= computer()
c1.age=30
c2= computer()

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")

print(c1.name)
print(c2.name)




### types of variables

class car:
    weel=4         ### class veriable

    def __init__(self):
        self.mil=40       ## instance veriable
        self.com="BMW"    ## instance veriable 
   
c1=car()
c2=car()

c1.mil=20
car.weel=8

print(c1.mil,c1.com,c1.weel)
print(c2.mil,c2.com, c2.weel)



## types of methods 

class student:
    school="Sundarban"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    
    @classmethod
    def info(cls):
        return cls.school
    
s1=student(45,55,67)
s2=student(22,33,44)

print(s1.avg(),s1.school)
print(s2.avg(),s2.school)





