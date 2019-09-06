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
        arr[end], arr[0] = arr[0], arr[end]
        return self.max_heap(arr, 0, end)

    def heap_sort(self, arr):
        self.build_max_heap(arr)
        for i in range(self.len_arr-1, 0, -1):
            print("heap_sort, extract return", self.extract_heap(arr, i))
        return ("heap return", arr)
    def heap(self, arr):
        self.build_max_heap(arr)
        for i in range(self.len_arr-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.max_heap(arr, 0, i)

