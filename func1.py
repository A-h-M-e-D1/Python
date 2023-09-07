def sum_two_number(num1,num2) ->float:
    return num1+num2

class person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        pass
    def show_info(self):
        print(f"my name is {self.name} and my age is {self.age}")
instance=person('Ali',45)
