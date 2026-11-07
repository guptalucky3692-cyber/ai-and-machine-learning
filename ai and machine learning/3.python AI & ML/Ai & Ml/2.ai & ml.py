# #                     oops object oriented programm
# class Factory: 
#     def __init__(self,material,zips,pockets): #self for  object location target
#         self.material = material
#         self.pockets = pockets
#         self.zips = zips
#     def show(self):
#         print(f"your objects details are {self.material},{self.pockets},{self.zips}")
# rebook =  Factory("bat",12,33)
# campus = Factory("horse",3,5)
# rebook.show()
# campus.show()

# class Animals:
#     name = "lion" #class attribute or class blue print create karegi
#     def __init__(self,age):  #self for  object location target
#         self.age =age      #instance attribute
#         pass

#     def show(self):  #instance attribute
#         print(f"how are you {self.age}")
#         pass

#     @classmethod             #classmethods
#     def hello(cls): # cls target for class location
#         print("you are great job")

#     @staticmethod  
#     def static():
#         print("how are you")

# obj = Animals(12)
# obj.show()
# obj.hello()
# obj.static()

# class Factorymoumbai:
#     a = "helo how are you"
#     def hello(self):
#         print("I am fine")
    
# class  Factorypune(Factorymoumbai):
#     pass
# obj = Factorymoumbai()
# obj2 = Factorypune
# obj.hello()


# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print(f"Hello your name is {self.name}")

# class Human(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age
#     def show(self):
#         print(f"Hello your name is {self.name},{self.age}")

# person1 = Human("lion",56)
# p2 = Animal("lion")
# person1.show()
# p2.show()

# anharke inheritance
# class Animal:
#     def __init__(self,name):
#         pass

# class Human:
#     def __init__(self,age):
#         pass
# class robots(Human,Animal):
#     name = "rrest"

# obj = robots()

# #multi level inharitance
# class Factory:
#     def __init__(self,matrial,zips):
#         self.matrial = matrial
#         self.zips = zips
    
# class delhifactory(Factory):
#     def __init__(self, matrial, zips,color):
#         super().__init__(matrial, zips)
#         self.color = color
        
# class punefactory(delhifactory):
#     def __init__(self, matrial, zips, color,product):
#         super().__init__(matrial, zips, color)
#         self.product =product

# class Animal:      ##duck typing
#     def show(self):
#         print("I am showing ")

# class Human:
#     def show(self):
#         print("hello I am also showing ")
# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()

# from abc import ABC, abstractmethod

# class abstract(ABC):
#     @abstractmethod
#     def perimeter(self):
#         pass 
    
#     @abstractmethod
#     def area(self):
#         pass

# class Square(abstract):
#     def __init__(self,side):
#         self.side = side

#     def perimeter(self):
#         print("i have created")
    
#     def area(self):
#         print("I have created this ")



# class Circle(abstract):
#     def __init__(self,radius):
#         self.radius = radius
    
#     def perimeter(self):
#         print("i have created")
    
#     def area(self):
#         print("I have created this ")

# obj = Circle(7)
# obj2 = Square(12)
# obj.area()
# obj.perimeter()

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"hello how are you and your name is {self.name}"

    def __add__(self,other):
        sum = 0
        for i in other:
            sum = sum + i.age

        return f"your sum of ages are {self.age + sum}"

obj = Animal("lion",12)
obj2 = Animal("dolphin",14)
obj3 = Animal("tiger",34)

print(obj + (obj2,obj3))

    

    


    

    





