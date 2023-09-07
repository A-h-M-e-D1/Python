# Sorting Algorthims 
# Bubble Sort => in-place and stable 
# best case  when sorted in order o(n)
# Worst case whe sorted in reversed order o(n^2)

#Implementation of Bubble Sort

#ترتيب تصاعدي
def BubbleSort(array):
     n = len(array)
     # Traverse through all array elements
     for i in range(n):
         swapped = False

         for j in range(0,n-i-1):
             if array[j] > array[j+1]:
                 array[j],array[j+1] = array[j+1],array[j]
                 swapped = True

         if (swapped == False):
             break

array = [64, 34, 25, 12, 22, 11, 90]
BubbleSort(array)
print("Sorted array Ascending order: ")
for i in range(len(array)):
    print(array[i],end=" ")




#ترتيب تنازلي 

def Bubblesort(arr):
    n = len(arr)
    # loop in index in array
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j] < arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
                swapped = True
        if (swapped == False):
            break
arr = [12,25,34,64,11,90]
Bubblesort(arr)
print("\n","Sorted array Descending Order: ")
for i in range(len(arr)):
    print(arr[i],end=" ")
