# ---Recursive Function---
# 1-call itself
# 2-even alternative for simple loops and iterations
# def countdown(number):
#     print(number)
#     if number==1:
#         return
#     else:
#          countdown(number-1)
# countdown(5) 
        
# def mysum(list1):
#     print(list1)
#     if not list1:
#         return 0
#     else:
#         return list1[0] + mysum(list1[1:])
# print(mysum([1,2,3,4,5]))    

# def count_leaf_items(item_list):
#     """Recursively counts and returns the
#        number of leaf items in a (potentially
#        nested) list.
#     """
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_leaf_items(item)
#         else:
#             count += 1

#     return count
# print(count_leaf_items([1,[2,3],4,5]))