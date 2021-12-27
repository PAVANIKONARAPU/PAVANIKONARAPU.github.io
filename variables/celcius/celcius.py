class CelClass:
    #class variable it by defaul static variable
    #c=(5/9)x(f-32)
    cel=32;far=65;x=5/9;y=32


    @classmethod
    def fahrenheit_to_celcius_class(cls):
        c=(cls.x)*(cls.far-cls.y)
        return c
    

    @staticmethod
    def fahrenheit_to_celcius_static(self):
        CelClass.cel=(self.x)*(CelClass.far-self.y)
        print(CelClass.far,"fahrenheit temperature=",CelClass.cel)

    #instancemethod
    def fahrenheit_to_celcius_instance(self):
        self.cel=(self.x)*(self.far-self.y)
        print(self.far,"fahrenheit temperature=",self.cel)

    
obj=CelClass()
print("far default value of object:",obj.cel)
clsReturn=CelClass.fahrenheit_to_celcius_class()
print(clsReturn)
obj.fahrenheit_to_celcius_instance()
obj.fahrenheit_to_celcius_static(obj)



    