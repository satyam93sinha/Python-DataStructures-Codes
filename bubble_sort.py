"""Bubble Sort Algo:
1. iterate through the list/array
2. iterate again to compare the elements with each other
3. if arr[j] > arr[j+1]:
4. swap the numbers in comparison
5. these swaps are the passes here that bubbles up the largest element to the
top.
6. perform these steps n times, n=len(list)

Conceptually,

Assume a list l = [2, 5, 3, 0],
Iter1: take the first element and compare it with
the one after it and if arr[0] is greater than arr[1], swap elements else no
operation is performed.

Iter2: arr[1] > arr[2], swap so now arr[1]=3 and arr[2]=5.
Iter3: arr[2] > arr[3], swap so now arr[2]=0 and arr[3]=5.
In Iter3, we see the largest element of the list bubbles up to the end, already
sorted position.

The list after these three passes become [2, 3, 0, 5]

Iter4: arr[0]>arr[1], false so no swap occurs.
Iter5: arr[1]>arr[2], true so now arr[1]=0 and arr[2]=3 after swapping elements
Iter6: arr[2]>arr[3], false so no swap.

Already, 5 is at the sorted position so we may skip the Iter6 step as programmed
below.
The list now becomes [2, 0, 3, 5]

Iter7: arr[0]>arr[1], true, swap so now arr[0]=0 and arr[1]=2
List becomes, [0, 2, 3, 5] which is sorted.

"""



def bubble_sort(arr):
    print(arr)
    for i in range(len(arr)):
        flag = 0
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = 1
                print(arr)
        # print(arr)
        if flag == 0:
            break

bubble_sort([2, 4, 3, 1, 7, 0, 5])
