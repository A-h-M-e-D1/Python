# Revision

# class bog:
#     def __init__(self,name,age) -> None:
#         self.name=name
#         self.age=age

# my_bog=bog('can',13) # instance 

# print(my_bog.name) 
# print(my_bog.age)


# instance ِattribute
# class car:
#     def __init__(self,name,speed) -> None:
#         self.name=name
#         self.speed=speed
# # instance ِattribute
# car1=car('Toyota',300)
# car2=car('Mercedes',400)

# print(car1.name)
# print(car1.speed)

# instance Methods 
# class triangle:
#     def __init__(self,base_length,height) -> float:
#         self.base_length=base_length
#         self.height=height
#         # instance Methods 
#     def clac_area(self):
#         """This function used to claculator Area of Triangle"""
#         return f'Area of Triangle = {1/2 * self.base_length * self.height}' 
# triangle_1=triangle(10,5)
# area_of_triangle_1=triangle_1.clac_area()

# print(area_of_triangle_1)

# Class Attributes
# class Person:
#     nationality='Egypt' # class Attribute
#     def __init__(self,name,age) -> None:
#         self.name=name
#         self.age=age

# person1=Person('Ahmed',30)
# person2=Person('Ali',15)

# print(person1.name)
# print(person1.age) 

# print(person1.nationality) #Egypt
# # print(person2.nationality) # Egypt

# # change nationality attribute to person 2

# person2.nationality='Spain'
# print(person2.nationality)

# Class Methods Vs Static Methods

# class MathUtils:
#     @classmethod
#     def calculate_area(cls, radius):
#         return 3.14 * radius**2

#     @classmethod
#     def calculate_circumference(cls, radius):
#         return 2 * 3.14 * radius

# radius = 5
# area = MathUtils.calculate_area(radius)
# print("Area:", area)

# circumference = MathUtils.calculate_circumference(radius)
# print("Circumference:", circumference)


# Static methods
# class  StringUtils:
#     @staticmethod
#     def reverse_string(string):
#         return string[::-1]
#     @staticmethod
#     def length_string(string):
#         return len(string)
# string='Ahmed'
# print(StringUtils.reverse_string(string))
# print(StringUtils.length_string(string))
