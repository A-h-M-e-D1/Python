# # calculate Power 
# def pow(number,power):
#     """this Function to calc the power of the number"""
#     # base case
#     if power == 0:
#         return 1
#     # store result
#     result = pow(number,power//2)
#     # if the power is even
#     if power % 2 == 0:
#         return result*result
#     # if the power is odd
#     if power % 2 !=0:
#         return result * result* number
# print("The Result = ")
# print(pow(2,3))



#####--------Merge Sort Algorthims----------####

# Ascending order by MergeSort

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_arr = arr[:mid]
#         right_arr = arr[mid:]

#         # Recursively sort left and right arrays
#         merge_sort(left_arr)
#         merge_sort(right_arr)

#         i = j = k = 0
#         # Merge the sorted sub-arrays back into the original array
#         while i < len(left_arr) and j < len(right_arr):
#             if left_arr[i] <= right_arr[j]:
#                 arr[k] = left_arr[i]
#                 i += 1
#             else:
#                 arr[k] = right_arr[j]
#                 j += 1
#             k += 1

#         # Check if any element was left
#         while i < len(left_arr):
#             arr[k] = left_arr[i]
#             i += 1
#             k += 1
#         while j < len(right_arr):
#             arr[k] = right_arr[j]
#             j += 1
#             k += 1


# arr = [12, 11, 13, 5, 6, 7]
# print("Original array is:")
# print(arr)

# merge_sort(arr)
# print("Sorted array is:")
# print(arr)

# Descending Order by MergeSort
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_arr = arr[:mid]
#         right_arr = arr[mid:]

#         # Recursively sort left and right arrays
#         merge_sort(left_arr)
#         merge_sort(right_arr)

#         i = j = k = 0
#         # Merge the sorted sub-arrays back into the original array
#         while i < len(left_arr) and j < len(right_arr):
#             if left_arr[i] >= right_arr[j]:
#                 arr[k] = left_arr[i]
#                 i += 1
#             else:
#                 arr[k] = right_arr[j]
#                 j += 1
#             k += 1

#         # Check if any element was left
#         while i < len(left_arr):
#             arr[k] = left_arr[i]
#             i += 1
#             k += 1
#         while j < len(right_arr):
#             arr[k] = right_arr[j]
#             j += 1
#             k += 1


# arr = [12, 11, 13, 5, 6, 7]
# print("Original array is:")
# print(arr)

# merge_sort(arr)
# print("Sorted array is:")
# print(arr)


# QuickSort Algorthims

# Ascending order
# def partition(arr,low,high):
#     # pivot 
#     p = arr[high]
#     # the high element in right side 
#     i = low-1
#     for j in range(low,high):
#         if arr[j] <= arr[i]:
#             (arr[j],arr[i]) = (arr[i],arr[j])
#     (arr[i+1],arr[high]) = (arr[high],arr[i+1])
#     return i+1

# def quicksort(arr,low,high):
#     if low < high:
#         # called partition function
#         pi = partition(arr,low,high)
#         # recursively sort the low side
#         quicksort(arr,low,pi-1)
#         # recursively sort the high side
#         quicksort(arr,pi+1,high)

# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# # called the function
# quicksort(arr,0,n-1)
# print("Sorted array is: ")
# for k in arr:
#     print(k,end=" ")



# Descending Order
# def partition(arr,low,high):
#     # pivot 
#     p = arr[low]
#     # the high element in right side 
#     i = low
#     for j in range(low+1,high+1):
#         if arr[j] >= p:
#             i+=1
#             (arr[j],arr[i]) = (arr[i],arr[j])
#     (arr[i],arr[low]) = (arr[low],arr[i])
#     return i

# def quicksort(arr,low,high):
#     if low < high:
#         # called partition function
#         pi = partition(arr,low,high)
#         # recursively sort the low side
#         quicksort(arr,low,pi-1)
#         # recursively sort the high side
#         quicksort(arr,pi+1,high)

# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# # called the function
# quicksort(arr,0,n-1)
# print("Sorted array is: ")
# for k in arr:
#     print(k,end=" ")


# onther quicksort implemention
#
# def quicksort(array):
#     # base case
#     if len(array) < 2:
#         return array
#     else:
#         # Recursive case
#         pivot = array[0]
        
#         # left side thats contains element less than pivot
#         left_arr = [ i for i in array[1:] if i <= pivot]
        
#         # right side thats contain element grearter than pivot
#         right_arr = [i for i in array[1:] if i > pivot]
        
#         # combine left+pivot+right
#         return quicksort(left_arr) + [pivot] + quicksort(right_arr)
# array = [10,5,2,3]
# print(quicksort(array))
        

































