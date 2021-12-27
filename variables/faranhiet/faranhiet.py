from types import CellType


class FaranClass:
    #class variable it by default static variable
    cel=38
    far=65
    x=9/5
    y=32

    def __init__(self):
        self.cel=55
        self.far=105

    #class method
    @classmethod
    def celcius_to_fahrenheit(cls):

        #degree F=(degree C x 9/5)+32
        f=(cls.cel*cls.x)+cls.y
        return f
    
    @staticmethod
    def celcius_to_fahrenheit_static(self):
        FaranClass.far=(FaranClass.cel*self.x)+self.y
        print(FaranClass.cel,"celcius temperature =",FaranClass.far)
    
    #instance method
    def celcius_to_fahrenheit_instance(self):
        self.far=(self.cel*self.x)+self.y
        print(self.cel,"celcius temperature in fahrenheit=",self.far)

    def getmethod(self):
        return self.far
    
    def setmethod(self,far):
        self.far=far
        print("using setter method set fahrenheit=",self.far)

    def __init__(self,far,cel):
        self.cel=Cel
        self.far=far

objFaranClass=FaranClass()
print("far default value of object:",objFaranClass.far)
clsReturn=FaranClass.celcius_to_fahrenheit()
print(clsReturn)
objFaranClass.celcius_to_fahrenheit_instance()
objFaranClass.celcius_to_fahrenheit_static(objFaranClass)
print("get value using getter method:",objFaranClass.getmethod())
xx=105
objFaranClass.setmethod(objFaranClass.y)
far=float(input("enter far="))
cel=float(input("enter cel="))
objfah=FaranClass(far,cel)
print(objfah.far,":",objfah.cel)
   