class HeapSort:
    def __init__(self, arr):
        self.arr = arr
        self.len_arr = len(arr)

    def max_heap(self, arr, i, n):
        # i is the root to max_heapify or generate max heap on.
        left = 2*i + 1
        right = 2*i + 2
        max_ = i

        # test if left of root exists and is greater than root, i
        if left<n and arr[left]>arr[i]:
            max_ = left

        # test if right of root exists and is greater than root, left
        # or comparison to both, max_, where max_ is a reference to maximum
        # element until swap occurs. Then, recursion for max_heap is called
        # taking max_ as root index to maximise heap.
        if right<n and arr[right]>arr[max_]:
            max_ = right

        # test if root index is maximum
        if (max_ != i):
            # if root is not max_ index, we swap to make root contain max element
            arr[max_], arr[i] = arr[i], arr[max_]

            # we max_heapify root by running max_heap recursively on max_ index
            # until all the above if conditions fail so that the root of this
            # subtree truly becomes a max_heap.
            return self.max_heap(arr, max_, n)

    def build_max_heap(self, arr):
        # builds max heap, we iterate from n//2 to 0 because n//2+1 to n are
        # leaves and they are good as they already are max_heaps or min_heaps
        # when needed.
        for i in range(self.len_arr//2, -1, -1):
            self.max_heap(arr, i, len(arr))

    def extract_heap(self, arr, end):
        # swap the first/max element with the least/last element,
        # this in a way extracts the max element/root to bottom sorting elements
        # decrease the length of array with the loop, call max_heap to ensure
        # heap is max_heap.
        arr[end], arr[0] = arr[0], arr[end]
        return self.max_heap(arr, 0, end)

    def heap_sort(self, arr):
        """Sorting Heap
        Firstly, we build max_heap so that the greater elements are at roots
        and could be easily extracted with least time complexity.
        Later, we iterate through the heap, nearly complete binary tree in
        reverse order so that we can specify the exact length of array."""
        self.build_max_heap(arr)
        for i in range(self.len_arr-1, 0, -1):
            print("heap_sort, extract return", self.extract_heap(arr, i))
        return ("heap return", arr)
    
    def heap(self, arr):
        """A function performing extraction + heap_sort function's work."""
        self.build_max_heap(arr)
        for i in range(self.len_arr-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.max_heap(arr, 0, i)
    """
    The way of applying the logic for extraction differs below:
    1. The max element of the heap in max_heap will always be at 0th index of the array here.
    2. Thus, we pass 0 as node to extract_heap() function as one of the arguments.
    3. With every iteration we have to ignore the last i elements of array while building max heap,
       thus, len(arr)-i-1.
    def extract_heap(arr, node, arr_len):
        arr[node], arr[arr_len] = arr[arr_len], arr[node]
        build_max_heap(arr, arr_len)
        return arr
    def heap_sort(arr):
        build_max_heap(arr, len(arr))
        for i in range(0, len(arr)):
            extract_heap(arr, 0, len(arr)-i-1)
        return "Heap Sorted Array: {}".format(arr)
    """

    def min_heapify(self, arr, i, n):
        left = 2*i+1
        right = 2*i+2
        min_ = i
        
        # check if left child is less than root
        if left<n and arr[left]<arr[i]:
            min_ = left

        # check if right child is less than root and left child
        if right<n and arr[right]<arr[min_]:
            min_ = right

        # check if root is the minimum of root, left and right children
        if min_ != i:
            arr[min_], arr[i] = arr[i], arr[min_]
            self.min_heapify(arr, min_, n)

    def build_min_heap(self, arr):
        n = len(arr)
        for i in range(n//2, -1, -1):
            self.min_heapify(arr, i, n)

    def extract_min_heap(self, arr, end):
        arr[end], arr[0] = arr[0], arr[end]
        self.min_heapify(arr, 0, end)
        return arr

    def min_heap_sort(self, arr):
        self.build_min_heap(arr)
        for i in range(len(arr)-1, 0, -1):
            self.extract_min_heap(arr, i)
        return arr

