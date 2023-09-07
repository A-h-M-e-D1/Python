# Conditinal Logic and Control Flow

# print(1<=1) #True
# print(1!=1) #false
# print(1!=2) #True
# print("#"*50)
# print("good"!="bad") # True
# print("good" != "Good") #True
# print(123=="123") # false

#### logical operators "And==OR== Not"
# 1-And
#print(1 < 2 and 3 < 4 )  => # true 
#print(10==10 and 10 < 0) => # false

# 2-OR 
#print(8 > 7 or 0 > 5)   =>  # True
#print(0 > 1 and 1 > 5)  => # False

# 3-Not
# print(not True)  => # False
# print(not False) => # True

# Control Flow
# simple Program

# student_grade=int(input("Enter Your Grade"))

# if student_grade >= 90:
#     print("You Passed The Class With => A")
# elif student_grade >= 80 :
#      print("You Passed The Class With => B")
# elif student_grade >= 70:
#       print("You Passed The Class With => C")
# else:
#       print("You did not Pass The Class ")

# print("Thanks for attending.")

# sport=input("Enter a Sport: ")

# p1_score=int(input("Enter player 1 score: "))
# p2_score=int(input("Enter player 2 score: "))

# if sport.lower() == "basketball":
#     if p1_score == p2_score:
#         print("The Game Is a draw.")
#     elif p1_score > p2_score:
#         print("Player 1 wins.")
#     else:
#         print("Player 2 wins.")

# elif sport.lower() == "golf":
#     if p1_score == p2_score :
#         print("The Game Is draw.")
#     elif p1_score < p2_score:
#         print("Player 1 wins. ")  
#     else:
#         print("Player 2 wins.")       
# else:
#     print("Unknown sport")

# for n in range(4):
#     password=input("Enter Your password=> ")
#     if password == "Ahmed2004$":
#         print(open("important.txt","r"))
#         break
#     print("Password is incorrect")
# else:
#     print("All Tries finished")    


# Loops

# odd_number=0
# even_number=0

# number=int(input("Enter the Number: "))

# while number != 0:
#     if number % 2 ==0 :
#         even_number+=1
#     else:
#         odd_number+=1
        
#     number=int(input("Enter the Number: "))
    
# print("Number of even Is => ",even_number)   
# print("Number of odd Is => ",odd_number)   

# num=0
# while num <=100:
#     num+=1
#     if num % 2==0:
#         print(num)

# user_input=int(input("Enter The Number: "))

# is_prime=True

# if user_input > 1:
#     i=2
#     while i <= user_input / 2:
#         if user_input % i==0:
#             is_prime=False
#             break
#         i+=1 
# if is_prime:
#     print(user_input," prime Number" )
# else:
#     print(user_input," Not Prime Number")                
    

# v="Python"

# for letter in v:
#     print(letter)

# word="python"
# index=0
# while index < len(word):
#     print(word[index])
#     index+=

# Functions

# def multiple(x,y): # function signature
#     """
#     Return The Product of two numbers x and y
#     """
#     product=x *y 
#     return product 
# print(multiple(2,5))
# print(help(multiple))
# print("#"*50)


# def cube(num1):
#     """
#     Return cube of number
#     """
#     result=num1**3
#     return result
# print(cube(2)) # 8

type = int(input())
