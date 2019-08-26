def binary_search(arr, start, end, num):
    if start > end:
        return -1
    elif start <= end:
        mid = (start+end)//2
        if num == arr[mid]:
            return (num, mid)
        elif num < arr[mid]:
            end = mid - 1
        elif num > arr[mid]:
            start = mid + 1
        return binary_search(arr, start, end, num)


def binary_search_loop(arr, n, x):
    start, end = 0, len(arr)-1
    while (start <= end):
        mid = (start+end)//2
        if x == arr[mid]:
            return ((mid, x))
        elif x < arr[mid]:
            end = mid - 1
        elif x > arr[mid]:
            start = mid + 1
    return -1

result = -1

def first_occur_binary(arr, start, end, num):
    """if start > end:
        return "start>end: {} {}".format(-1, result)"""
    global result
    if start <= end:
        mid = (start+end)//2
        if num == arr[mid]:
            result = mid
            end = mid-1
        elif num < arr[mid]:
            end = mid-1
        elif num > arr[mid]:
            start = mid+1
        print("start:{}, end:{}, mid:{}, arr[mid]:{}, result:{}".format(start, end, mid, arr[mid], result))
        first_occur_binary(arr, start, end, num)
    return result
result_last = -1
def last_occur_binary(arr, start, end, num):
    """if start > end:
        return "start>end: {} {}".format(-1, result)"""
    global result_last
    if start <= end:
        mid = (start+end)//2
        if num == arr[mid]:
            result_last = mid
            start = mid+1
        elif num < arr[mid]:
            end = mid-1
        elif num > arr[mid]:
            start = mid+1
        print("start:{}, end:{}, mid:{}, arr[mid]:{}, result:{}".format(start, end, mid, arr[mid], result))
        last_occur_binary(arr, start, end, num)
    return result_last
