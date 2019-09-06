sorted_array = list()
def max_heapify(arr, i, heap_size):
    left = 2*i-1
    right = 2*i+1-1
    max_ = i-1
    if (left<heap_size and arr[i-1]<arr[left]):
        max_ = left
    else:
        max_ = i-1
    if (right<heap_size and arr[max_]<arr[right]):
        max_ = right
    if (max_ != i-1):
        arr[max_], arr[i-1] = arr[i-1], arr[max_]
        res = max_heapify(arr, max_+1, heap_size)
        # print("res", res) : will return the below line whenever
        # a recursive call is completed.
    return ("max_heapify arr:{}".format(arr))


def build_max_heap(arr):
    heap_size = len(arr)
    for i in range(len(arr)//2, 0, -1):
        array = max_heapify(arr, i, heap_size)
        print("build_max_heap", arr)
    return arr


def extract_heap(arr):
    if len(arr)<1:
        return "No Elements"
    max_ = arr[0]
    sorted_array.append(max_)
    arr[0] = arr[len(arr)-1]
    del arr[len(arr)-1]
    max_heapify(arr, 1, len(arr))
    return (arr, max_)

def heap_sort(arr):
    array = build_max_heap(arr)
    for i in range(len(array)):
        print("heap_sort", extract_heap(array))
    print(sorted_array)
        


