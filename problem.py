
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# total_a = 0
# total_b = 0

# if a[0] > b[0]:
#     total_a+=1
# elif a[0] < b[0]:
#     total_b+=1
# if a[1] > b[1]:
#     total_a+=1
# elif a[1] < b[1]:
#     total_b+=1
# if a[2] > b[2]:
#     total_a+=1
# elif a[2] < b[2]:
#     total_b+=1
# else:
#     total_a = total_b = 0
# print(total_a,total_b)

# num_of_element = int(input())
# arr = list(map(int,input().split()))

# sum = 0

# for i in range(len(arr)):
#     sum+=arr[i]
# print(sum)

# num_of_element = int(input())
# arr = list(map(int,input().split()))

# # loop in array
# n = len(arr)
# for i in range(n):
#     swapped = False
#     for j in range(0,n-i-1):
#         if arr[j] > arr[j+1]:
#             #swapped
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#             swapped = True
#     if(swapped == False):
#         break
# for i in range(len(arr)):
#     print(arr[i],end=" ")


# size_of_arr = int(input())
# arr = list(map(int,input().split()))

# count_positive = 0
# count_negative = 0
# count_Zero = 0

# n = len(arr)

# for i in range(n):
#     if arr[i] > 0:
#         count_positive+=1
#     if arr[i] < 0:
#         count_negative+=1
#     if arr[i] == 0:
#         count_Zero+=1
# ratio_positive = count_positive / n 
# ratio_negative = count_negative / n 
# ratio_zero = count_Zero / n 
# print("{:6f}".format(ratio_positive))
# print("{:6f}".format(ratio_negative))
# print("{:6f}".format(ratio_zero))

# def search(arr,target):
#     left = 0
#     right = len(arr)-1

# arr =list(map(int,input().split()))
# max_num = arr[0]
# min_num = arr[0]
# sum = 0
# for i in range(len(arr)):
#          if arr[i] > max_num : max_num = arr[i]
#          if arr[i] < min_num : min_num=arr[i]
#          sum+=arr[i]
# print(sum-max_num,sum-min_num)


def sort(arr):
    # length of arr
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
arr = [64, 34, 25, 12, 22, 11, 90]
sort(arr)
print("Sorted Array: ")
for i in range(len(arr)):
    if i != len(arr) - 1:
        print(arr[i], end=" < ")
    else:
        print(arr[i])



