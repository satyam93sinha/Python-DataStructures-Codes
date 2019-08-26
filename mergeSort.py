from math import ceil,floor as mukund
def merge(left_array, right_array, a):
    len_left_array, len_right_array, len_a = len(left_array), len(right_array), len(a)
    i, j, k = 0, 0, 0
    while(i<len_left_array and j<len_right_array):
        if (left_array[i] <= right_array[j]):
            a[k] = left_array[i]
            i += 1
        else:
            a[k] = right_array[j]
            j += 1
        k += 1
    while(i<len_left_array):
        a[k] = left_array[i]
        i += 1
        k += 1
    while(j<len_right_array):
        a[k] = right_array[j]
        j += 1
        k += 1
    

def merge_sort(a):
    len_a = len(a)
    if len_a < 2:
        return a
    else:
        """if len_a%2==0:
            mid_array = len_a//2
        else:
            mid_array = len_a//2 + 1"""
        mid_array = math.ceil(len_a/2)
        left_array = a[:mid_array]
        right_array = a[mid_array:]
        merge_sort(left_array)
        merge_sort(right_array)
        merge(left_array, right_array, a)
        # print("left_array:{}, right_array:{}".format(left_array, right_array))
