# ---Revision----
# Scope
# x="Hello World" # Global Scope
# def func():
    # x=2 # local Scope
    # print(f"inside 'func' ,x has the Value=> {x}")
# func() 
# print(f"outside 'func' , x has the value => {x}")   

# nonlocal

# def outer_func():
#     x="outer"
#     def nest_func():
#         nonlocal x 
#         x="inner"
#         print("inner: ",x)
#     nest_func()
#     print("outer: ",x)
# outer_func()

# def func():
#     x="ni"
#     def func2():
#         x="spam"
#     func2()
#     print(x)
# func()   #output = "ni"

# Arugments=>parameters
# student={'Archana':28,'krishna':25,'Ramesh':32,'vineeth':25}
# def test(student):
#    new={'alok':30,'Nevadan':28}
#    student.update(new)
#    print("Inside the function",student)
#    return
# test(student)
# print("outside the function:",student)

# my_tuple=(1,2,3,4,6)
# def test2(my_tuple):
#    print("MY Tuple inside function =>",my_tuple)
# test2((5,6,7,8))
# print(my_tuple)

# def sum(num1,num2): # num1 , num2 => Are parameters
#    return "Sum of two numbers =>",num1+num2
# result=sum(2,5) # 2 , 5 => are Arguments 
# print(result)


# Keyword and Default 

# Keywords 
# def f(a,b,c):
#     print(a,b,c)
# f(1,2,3)
# f(c=3,b=2,a=1)    

# def func(a,*b,c):
#     print(a,b,c)
# func(1,2,c=3)    # 2 => (2,)

# def func2(a,b,**c):
#     print(a,b,c)
# func2(1,2,c=5)    # output => 1 2 {'c':5} 

# def func (a=6,b=4,c=5):
#     print(a,b,c)
# func()    
    
# lambda Functions Vs def 
# def my_lambda(x,y):
#     print(f"the sum of two numbers is: {x+y}")
# my_lambda(2,3)

# print("#"*50)

# my_lambda=lambda x,y :f"the sum of two numbers is: {x+y}"
# print(my_lambda(2,3))

# l=[lambda x:x**2,
#    lambda x:x**3,
#    lambda x:x**4]
# for i in l:
#     print(i(2))
# print(l[0](3))

# print((lambda lst: sum(lst))([4, 5, 6]))
# from array import array
# number_of_elements=int(input())
# numbers=list(map(int,input().split()))
# array=array("i",numbers)
# def max_min():
#     print(min(numbers),max(numbers))
# max_min()    
    
# number_of_elements=int(input())
# numbers=list(map(int,input().split()))
# min=numbers[0]
# max=numbers[0]
# for i in numbers[1:]:
#      if i < min:
#          min=i
#          if i > max:
#              max=i
# print(min,max)

