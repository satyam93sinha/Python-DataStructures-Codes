Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============ RESTART: D:\SatyamSinha\DS Programs\HeapSortClass.py ============
>>> arr = [10, 2, 39, 59, 29]
>>> heap_sort(arr)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    heap_sort(arr)
NameError: name 'heap_sort' is not defined
>>> min_heap_sort(arr)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    min_heap_sort(arr)
NameError: name 'min_heap_sort' is not defined
>>> 
============ RESTART: D:\SatyamSinha\DS Programs\HeapSortClass.py ============
>>> arr = [10, 2, 39, 59, 29]
>>> min_heap_sort(arr)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    min_heap_sort(arr)
NameError: name 'min_heap_sort' is not defined
>>> heap = HeapSort(arr)
>>> heap.min_heap_sort(arr)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    heap.min_heap_sort(arr)
  File "D:\SatyamSinha\DS Programs\HeapSortClass.py", line 93, in min_heap_sort
    self.build_min_heap(arr)
  File "D:\SatyamSinha\DS Programs\HeapSortClass.py", line 86, in build_min_heap
    for i in range(len_arr//2, -1, -1):
NameError: name 'len_arr' is not defined
>>> 
============ RESTART: D:\SatyamSinha\DS Programs\HeapSortClass.py ============
>>> arr = [10, 2, 39, 59, 29]
>>> heap = HeapSort(arr)
>>> heap.min_heap_sort(arr)
[10, 39, 59, 29, 2]
>>> heap.build_min_heap(arr)
>>> arr
[2, 10, 59, 29, 39]
>>> arr = [50, 29, 290, 2890, 389, 277, 20]
>>> heap.build_min_heap(arr)
>>> arr
[20, 29, 50, 2890, 389, 277, 290]
>>> 
============ RESTART: D:\SatyamSinha\DS Programs\HeapSortClass.py ============
>>> arr = [50, 29, 290, 2890, 389, 277, 20]
>>> heap = HeapSort(arr)
>>> heap.min_heap_sort(arr)
[2890, 389, 290, 277, 50, 29, 20]
>>> 
