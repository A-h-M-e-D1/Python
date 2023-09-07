# Set
# set={1}
# print(dir(set))
# print(type(set))

# set={"a",1,1,2,2,3,4,8} # sets not ordered and and it unique
# print(set)

# set Methods
# set={1,2,3,5,9,7}
# set.clear()
# print(set) # set()

# set1={1,2,3,6,7}
# set2={8,9,10,11}
# print(set1 | set2) # {1,2,3,6,7,8,9,10,11}
# print(set1.union(set2)) # {1,2,3,6,7,8,9,10,11}

# my_set={1,7,9,10}
# my_set.add("a")
# print(my_set) # {1, 7, 9, 10, 'a'}

# set1={2,4,6,8,10}
# set1.copy()
# print(set1)
# set1.add("7")
# print(set1)

# set3={5,6,10,7}
# set3.remove(7)
# print(set3)

# set4={5,8,10}
# set4.remove(12)
# print(set4) # KeyError: 12

# set4={5,8,10}
# set4.discard(12)
# print(set4) # {8, 10, 5}

# set4={5,8,10}
# set4.pop()
# print(set4) #انت وحظك 

# Dictionary
# capitals={
#     'California':'Sacramento',
#     'New York':'Albany',
#     'Taxes':'Austin',
    
# }
# print(type(capitals)) # dict
# print(dir(capitals))
# print(capitals)
# Accesing Dict Values
# print(capitals['Taxes'])

#add values  
# capitals['Egypt']='cairo'
# del capitals['Taxes']
# print(capitals)

# loop in dict

# for key,value in capitals.items():
#     print(key,value)

# nested dict
# my_dict={
#     'Egypt':{
#         "Capital":'Cairo',
#         "landmarks":'cairo tower'
#     },
#     'UAE':{
#         "Capital":"Abu Dhabi",
#         "landmarks":'Tower Khalifa'
#     }
# }
# for key ,value in my_dict.items():
#     print(f"The Cauntary is {key} and The capital is {value['Capital']}")

