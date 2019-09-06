Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap_sort(arr)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    heap.heap_sort(arr)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 45, in heap_sort
    build_max_heap(self, arr)
NameError: name 'build_max_heap' is not defined
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap_sort(arr)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    heap.heap_sort(arr)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 45, in heap_sort
    self.build_max_heap(self, arr)
TypeError: build_max_heap() takes 2 positional arguments but 3 were given
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap_sort(arr)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    heap.heap_sort(arr)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 45, in heap_sort
    self.build_max_heap(arr)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 37, in build_max_heap
    self.max_heap(arr, max_)
NameError: name 'max_' is not defined
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap_sort(arr)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    heap.heap_sort(arr)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 46, in heap_sort
    self.build_max_heap(arr)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 38, in build_max_heap
    self.max_heap(arr, max_)
NameError: name 'max_' is not defined
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap_sort(arr)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    heap.heap_sort(arr)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 46, in heap_sort
    self.build_max_heap(arr)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 38, in build_max_heap
    self.max_heap(arr, max_)
NameError: name 'max_' is not defined
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap_sort(arr)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    heap.heap_sort(arr)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 46, in heap_sort
    self.build_max_heap(arr)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 38, in build_max_heap
    self.max_heap(arr, i)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 31, in max_heap
    max_heap(arr, max_)
NameError: name 'max_heap' is not defined
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap_sort(arr)
[19, 5, 10, 4, 1, 8, 3, 2]
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap_sort(arr)
heap_sort, extract return ([10, 5, 8, 4, 1, 2, 3], 10, 3, 7)
heap_sort, extract return ([19, 5, 10, 4, 1, 8, 3], 19, 3, 7)
heap_sort, extract return ([10, 5, 8, 4, 1, 2, 3], 10, 3, 7)
heap_sort, extract return ([19, 5, 10, 4, 1, 8, 3], 19, 3, 7)
heap_sort, extract return ([10, 5, 8, 4, 1, 2, 3], 10, 3, 7)
heap_sort, extract return ([19, 5, 10, 4, 1, 8, 3], 19, 3, 7)
heap_sort, extract return ([10, 5, 8, 4, 1, 2, 3], 10, 3, 7)
heap_sort, extract return ([19, 5, 10, 4, 1, 8, 3], 19, 3, 7)
('heap return', [19, 5, 10, 4, 1, 8, 3, 2])
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap(arr)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    heap.heap(arr)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 52, in heap
    self.build_max_heap(arr)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 38, in build_max_heap
    self.max_heap(arr, i, len(arr))
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 31, in max_heap
    self.max_heap(arr, max_)
TypeError: max_heap() missing 1 required positional argument: 'n'
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap(arr)
>>> arr
[1, 2, 3, 4, 5, 8, 10, 19]
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap_sort(arr)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    heap.heap_sort(arr)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 49, in heap_sort
    print("heap_sort, extract return", self.extract_heap(arr, len(arr)-i))
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 41, in extract_heap
    arr[0], arr[end] = arr[end], arr[0]
IndexError: list index out of range
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap_sort(arr)
heap_sort, extract return ([10, 5, 8, 4, 1, 2, 3], 10, 3, 7)
heap_sort, extract return ([10, 5, 8, 4, 1, 3, 2], 10, 2, 7)
heap_sort, extract return ([10, 5, 8, 4, 1, 3, 2], 10, 2, 7)
heap_sort, extract return ([10, 5, 3, 4, 8, 1, 2], 10, 2, 7)
heap_sort, extract return ([10, 5, 4, 1, 8, 3, 2], 10, 2, 7)
heap_sort, extract return ([10, 5, 4, 1, 8, 3, 2], 10, 2, 7)
heap_sort, extract return ([10, 8, 4, 1, 5, 3, 2], 10, 2, 7)
heap_sort, extract return ([10, 8, 4, 1, 5, 3, 2], 10, 2, 7)
('heap return', [5, 10, 4, 1, 8, 3, 2, 19])
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap_sort(arr)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    heap.heap_sort(arr)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 51, in heap_sort
    print("heap_sort, extract return", self.extract_heap(arr, i))
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 45, in extract_heap
    arr[i], arr[0] = arr[0], arr[i]
NameError: name 'i' is not defined
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap_sort(arr)
heap_sort, extract return None
heap_sort, extract return None
heap_sort, extract return None
heap_sort, extract return None
heap_sort, extract return None
heap_sort, extract return None
heap_sort, extract return None
('heap return', [1, 2, 3, 4, 5, 8, 10, 19])
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap_sort(arr)
heap_sort, extract return None
heap_sort, extract return None
heap_sort, extract return None
heap_sort, extract return None
heap_sort, extract return None
heap_sort, extract return None
heap_sort, extract return None
('heap return', [1, 2, 3, 4, 5, 8, 10, 19])
>>> extract_heap([19, 10, 8], 0, 3)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    extract_heap([19, 10, 8], 0, 3)
NameError: name 'extract_heap' is not defined
>>> heap.extract_heap([19, 10, 8], 0, 3)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    heap.extract_heap([19, 10, 8], 0, 3)
TypeError: extract_heap() takes 3 positional arguments but 4 were given
>>> heap.extract_heap([19, 10, 8], 3)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    heap.extract_heap([19, 10, 8], 3)
  File "D:/SatyamSinha/DS Programs/HeapSortClass.py", line 45, in extract_heap
    arr[end], arr[0] = arr[0], arr[end]
IndexError: list index out of range
>>> heap.extract_heap([19, 10, 8], 2)
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> heap = HeapSort(arr)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    heap = HeapSort(arr)
NameError: name 'arr' is not defined
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.extract_heap([19, 10, 8], 2)
>>> heap.build_max_heap(arr)
>>> arr
[19, 5, 10, 4, 1, 8, 3, 2]
>>> heap.extract_heap(arr, 7)
>>> arr
[10, 5, 8, 4, 1, 2, 3, 19]
>>> heap.extract_heap(arr, 6)
>>> arr
[8, 5, 3, 4, 1, 2, 10, 19]
>>> 
============ RESTART: D:/SatyamSinha/DS Programs/HeapSortClass.py ============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap = HeapSort(arr)
>>> heap.heap_sort(arr)
heap_sort, extract return None
heap_sort, extract return None
heap_sort, extract return None
heap_sort, extract return None
heap_sort, extract return None
heap_sort, extract return None
heap_sort, extract return None
('heap return', [1, 2, 3, 4, 5, 8, 10, 19])
>>> 
