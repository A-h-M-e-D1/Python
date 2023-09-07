# Sorting Algorthims 
# Bubble Sort => in-place and stable 
# best case  when sorted in order o(n)
# Worst case whe sorted in reversed order o(n^2)

#Implementation of Bubble Sort

#ترتيب تصاعدي
# def BubbleSort(array):
#      n = len(array)
#      # Traverse through all array elements
#      for i in range(n):
#          swapped = False
#          for j in range(0,n-i-1):
#              if array[j] > array[j+1]:
#                  array[j],array[j+1] = array[j+1],array[j]
#                  swapped = True

#          if (swapped == False):
#              break

# array = [64, 34, 25, 12, 22, 11, 90]
# BubbleSort(array)
# print("Sorted array Ascending order: ")
# for i in range(len(array)):
#     print(array[i],end=" ")


#ترتيب تنازلي 

# def Bubblesort(arr):
#     n = len(arr)
#     # loop in index in array
#     for i in range(n):
#         swapped = False
#         for j in range(0,n-i-1):
#             if arr[j] < arr[j+1]:
#                 arr[j+1],arr[j] = arr[j],arr[j+1]
#                 swapped = True
#         if (swapped == False):
#             break
# arr = [12,25,34,64,11,90]
# Bubblesort(arr)
# print("\n","Sorted array Descending Order: ")
# for i in range(len(arr)):
#     print(arr[i],end=" ")


# # Selection sort
# ترتيب تصاعدي
# arr = [64, 25, 12, 22, 11]
# n = len(arr)
# # loop in element
# for i in range(n):
#     min_index = i

#     for j in range(i+1,n):
#         if arr[j] < arr[min_index]:
#             min_index = j
#     # swapped
#     arr[i],arr[min_index] = arr[min_index],arr[i]


# print("Array Before Sorted => ",arr)
# for i in range(len(arr)):
#     print("Array After Sorted => ",arr[i])
    

#ترتيب تنازلي
# arr = [11,22,25,64,12]
# n = len(arr)

# for i in range(n):
#     max_index = 0
#     for j in range(i+1,n):
#         if arr[max_index] < arr[j]:
#             max_index = j
#             # swapped 
#             arr[i],arr[max_index] = arr[max_index],arr[i]
# print("Array Before sorted => ",arr)
# for i in range(len(arr)):
#     print(arr[i],end=" ")


# Insertion Sort
# put element in the right place
# Bset Case => Sorted => o(n)
# Worst Case => Reversely Sorted => o(n^2)
# Space complexity => o(1)
# in-place and stable

# implementation
#ترتيب تصاعدي
# def insert_array(arr):
#     n = len(arr)
#     # loop in element
#     for i in range(1,n):
#         k = arr[i]
#         j = i-1
#         while j >= 0 and arr[j]>k:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1] = k
# arr = [12, 11, 13, 5, 6]
# insert_array(arr)
# print("Sorted Array: ")
# for i in range(len(arr)):
#     print(arr[i],end=" ")

# ترتيب تنازلي
#def insert_array(arr):
    #     n = len(arr)
#     # loop in element
#     for i in range(1,n):
#         k = arr[i]
#         j = i-1
#         while j >= 0 and arr[j] < k:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1] = k
# arr = [12, 11, 13, 5, 6]
# insert_array(arr)
# print("Sorted Array: ")
# for i in range(len(arr)):
#     print(arr[i],end=" ")
