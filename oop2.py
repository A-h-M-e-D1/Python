#  simple revision
# class person:
#     age=30 # class attribute
#     def __init__(self,name) -> None:
#        self.name=name
# instance=person('Ahmed')
# print(instance.name)
# print(instance.age)

# class sum:
#     num1=int(input("Enter number one => "))
#     num2=int(input("Enter number Two => "))
#     def __init__(self) -> int:
#         pass 
# instance=sum()
# print=(f"The sum of two numbers is => {instance.num1 + instance.num2}")

#  Inheritance
# class Person:
#     def __init__(self,name) -> None:
#         self.name=name
# class manger(Person): # inheritance
#     def __init__(self, name) -> None:
#         super().__init__(name)
# my_instance=manger('Ahmed')
# print(my_instance.name)

#  Polymorphism
# static polymorphism
# class sum:
#     def __init__(self,input1,input2) -> None:
#         self.input1=input1
#         self.input2=input2
#     def sum_concetenate(self):
#         print(self.input1 +self.input2)
# my_instance=sum(2,5)
# my_instance2=sum('Ahmmed ',"ashraf")
# my_instance.sum_concetenate()
# my_instance2.sum_concetenate()

# dynamic polymorphism
# class person:
#     def __init__(self,name,job) -> None:
#         self.name=name
#         self.job=job
#     def names(self):
#         print(f"my name  is {self.name}")
#     def jobs(self):
#         print(f"my job is {self.job}")
# class employe1(person):
#     def __init__(self, name, job) -> None:
#         super().__init__(name, job)

# class employe2(employe1):
#     def __init__(self, name, job) -> None:
#         super().__init__(name, job)

# instance1=person('ahmed','security analyst')
# instance2=employe1('mohamed','enginner')
# instance3=employe2('abiahim','security enginner')

# for emplyees in (instance1,instance2,instance3):
#     emplyees.names()
#     print("#"*50)
#     emplyees.jobs()

#  Encapsulation
# class employee:
#     def __init__(self,name,project,salary) -> None:
#         # Data numbers
#         # self.name=name # public Member
#         self.__salary=salary #private Member
#         # self.project=project # protect Member

#     # methods
#     # show employees details 

#     def show(self):
#         # accessing public data member
#         print('Salary:', self.salary)
#     # def work(self):
#     #     print(self.name, 'is working on', self.project)
# # creating object of a class
# emp = employee('Jessa', 8000, 'NLP')

# # calling public method of the class
# emp.show()
# emp.work()

# class employee:
#     def __init__(self,name) -> None:
#         self.name=name # public Member
# my_instance=employee("Ahmed")
# print(f"Hello {my_instance.name}")

# class employee:
#     def __init__(self,name) -> None:
#         self.__name=name # private Member
#     def show(self):
#         print("Name is ",self.__name)
# my_instance=employee("Ahmed")
# # print(f"Hello {my_instance.name}") # Error

# # to access in private Member

# # print(f"Hello {my_instance._employee__name}")

# # another methods
# my_instance.show()


# class employee:
#     def __init__(self,name) -> None:
#          self._name=name # protect Member
#     def show(self):
#          print("Name ",self._name)
# my_instance=employee("Ahmed")
# # print(f"Hello {my_instance.name}")
# my_instance.show()

#  Getters And Setters

# class student:
#     def __init__(self,name,age) -> None:
#         # private property
#         self._name=name
#         self._age=age
#     # Getter
#     def get_name(self):
#         return self._name
#     # Setter
#     def set_name(self,value):
#         self._name=value
#     # Getter age
#     def get_age(self):
#         return self._age
#     # setters age
#     def set_age(self,value):
#         if value > 0 and value <=20:
#             self._age=value
#         else:
#             raise ValueError("Invalid age")
#     # إنشاء خصائص باستخدام دالة property()
#     name=property(get_name,set_name)
#     age=property(get_age,set_age)

# s1=student('ahmed',20)
# # print(s1.get_name()) #ahmed
# # print(s1.get_age()) # 20

# # s1.set_name('Omar')
# # s1.set_age(15)

# # print(s1.get_name()) # omar
# # print(s1.get_age()) # 15

#ABCs Abstract Base Class
# from abc import ABC,abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
# class Dog(Animal):
#     def make_sound(self):
#         print('Woof')
# class Cat(Animal):
#     def make_sound(self):
#         print("Meow")
# d=Dog()
# d.make_sound()
# c=Cat()
# c.make_sound()


# from abc import ABC,abstractmethod

# class shap(ABC):
#     @abstractmethod
#     def shap_area(self):
#         pass
# class Trangle(shap):
#     def __init__(self,base,height) -> None:
#         self.base=base
#         self.height=height
#     def shap_area(self):
#         return 1/2*self.base*self.height

# trangle_1=Trangle(5,6)
# print(trangle_1.shap_area()) #15.0
# s=shap()

