def quick_sort(arr, start, end):
    if start <= end:
        pIndex = partition(arr, start, end)
        quick_sort(arr, start, pIndex-1)
        quick_sort(arr, pIndex+1, end)



def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1

    arr[pIndex], arr[end] = arr[end], arr[pIndex]
    return pIndex
