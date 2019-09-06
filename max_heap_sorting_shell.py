Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
>>> arr
[6, 12, 1, 8, 5, 14, 16]
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> max_heapify(arr, 3)
>>> arr
[1, 5, 16, 8, 12, 14, 6]
>>> max_heapify(arr, 2)
>>> arr
[1, 12, 16, 8, 5, 14, 6]
>>> max_heapify(arr, 1)
>>> arr
[16, 12, 1, 8, 5, 14, 6]
>>> max_heapify(arr, 3)
>>> arr
[16, 12, 14, 8, 5, 1, 6]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
>>> arr
[16, 12, 1, 8, 5, 14, 6]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
>>> arr
[16, 12, 1, 8, 5, 14, 6]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    build_max_heap(arr)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 17, in build_max_heap
    max_heapify(arr, i)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 12, in max_heapify
    max_heapify(arr, max_)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 12, in max_heapify
    max_heapify(arr, max_)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 12, in max_heapify
    max_heapify(arr, max_)
  [Previous line repeated 13 more times]
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 4, in max_heapify
    if (left<=len(arr)-1 and arr[i-1]<arr[left]):
IndexError: list index out of range
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
>>> arr
[16, 12, 1, 8, 5, 14, 6]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    build_max_heap(arr)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 18, in build_max_heap
    max_heapify(arr, i, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 12, in max_heapify
    max_heapify(arr, max_)
TypeError: max_heapify() missing 1 required positional argument: 'heap_size'
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
>>> arr
[16, 12, 1, 8, 5, 14, 6]
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> max_heapify(arr, 3)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    max_heapify(arr, 3)
TypeError: max_heapify() missing 1 required positional argument: 'heap_size'
>>> max_heapify(arr, 3, 7)
>>> arr
[1, 5, 16, 8, 12, 14, 6]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
[1, 5, 16, 8, 12, 14, 6]
[1, 12, 16, 8, 5, 14, 6]
[16, 12, 1, 8, 5, 14, 6]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
[1, 5, 16, 8, 12, 14, 6] 6
[1, 12, 16, 8, 5, 14, 6] 4
[16, 12, 1, 8, 5, 14, 6] 2
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
[1, 5, 16, 8, 12, 14, 6] 6
[1, 12, 16, 8, 5, 14, 6] 4
[16, 12, 1, 8, 5, 14, 6] 2
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
build [1, 5, 6, 8, 12, 14, 16]
[1, 5, 16, 8, 12, 14, 6] 6
build [1, 5, 16, 8, 12, 14, 6]
[1, 12, 16, 8, 5, 14, 6] 4
build [1, 12, 16, 8, 5, 14, 6]
[16, 12, 1, 8, 5, 14, 6] 2
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
build [1, 5, 6, 8, 12, 14, 16]
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    build_max_heap(arr)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 21, in build_max_heap
    max_heapify(arr, i, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 12, in max_heapify
    max_heapify(arr, max_, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 14, in max_heapify
    max_heapify(arr, max_, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 14, in max_heapify
    max_heapify(arr, max_, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 14, in max_heapify
    max_heapify(arr, max_, heap_size)
  [Previous line repeated 1 more time]
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 12, in max_heapify
    max_heapify(arr, max_, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 14, in max_heapify
    max_heapify(arr, max_, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 14, in max_heapify
    max_heapify(arr, max_, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 14, in max_heapify
    max_heapify(arr, max_, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 12, in max_heapify
    max_heapify(arr, max_, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 14, in max_heapify
    max_heapify(arr, max_, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 14, in max_heapify
    max_heapify(arr, max_, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 12, in max_heapify
    max_heapify(arr, max_, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 14, in max_heapify
    max_heapify(arr, max_, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 14, in max_heapify
    max_heapify(arr, max_, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 12, in max_heapify
    max_heapify(arr, max_, heap_size)
  File "D:/SatyamSinha/DS Programs/max_heap.py", line 4, in max_heapify
    if (left<heap_size and arr[i-1]<arr[left]):
IndexError: list index out of range
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
build [1, 5, 6, 8, 12, 14, 16]
build [1, 5, 16, 8, 12, 14, 6]
build [1, 12, 16, 8, 5, 14, 6]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
build [1, 5, 6, 8, 12, 14, 16]
build [1, 5, 16, 8, 12, 14, 6]
build [1, 12, 16, 8, 5, 14, 6]
>>> arr
[16, 12, 1, 8, 5, 14, 6]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
build [1, 5, 6, 8, 12, 14, 16]
build [1, 5, 16, 8, 12, 14, 6]
build [1, 12, 16, 8, 5, 14, 6]
build [16, 12, 1, 8, 5, 14, 6]
>>> arr
[6, 12, 1, 8, 5, 14, 16]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
build [1, 5, 6, 8, 12, 14, 16]
build [1, 5, 6, 8, 12, 14, 16]
build [1, 5, 6, 8, 12, 14, 16]
build [1, 5, 6, 8, 12, 14, 16]
build [1, 5, 6, 8, 12, 14, 16]
build [1, 5, 16, 8, 12, 14, 6]
build [1, 12, 16, 8, 5, 14, 6]
build [16, 12, 1, 8, 5, 14, 6]
>>> arr
[6, 12, 1, 8, 5, 14, 16]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
build [1, 5, 6, 8, 12, 14, 16]
build [1, 5, 16, 8, 12, 14, 6]
build [1, 12, 16, 8, 5, 14, 6]
>>> arr
[16, 12, 1, 8, 5, 14, 6]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
[1, 5, 16, 8, 12, 14, 6]
[1, 12, 16, 8, 5, 14, 6]
[16, 12, 1, 8, 5, 14, 6]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
res [1, 5, 16, 8, 12, 14, 6]
[1, 5, 16, 8, 12, 14, 6]
res [1, 12, 16, 8, 5, 14, 6]
[1, 12, 16, 8, 5, 14, 6]
res [16, 12, 1, 8, 5, 14, 6]
[16, 12, 1, 8, 5, 14, 6]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
res [1, 5, 16, 8, 12, 14, 6]
[1, 5, 16, 8, 12, 14, 6]
res [1, 12, 16, 8, 5, 14, 6]
[1, 12, 16, 8, 5, 14, 6]
res [16, 12, 14, 8, 5, 1, 6]
res [16, 12, 14, 8, 5, 1, 6]
[16, 12, 14, 8, 5, 1, 6]
>>> arr = [1, 5, 6, 8, 18, 14, 16]
>>> build_max_heap(arr)
res [1, 5, 16, 8, 18, 14, 6]
[1, 5, 16, 8, 18, 14, 6]
res [1, 18, 16, 8, 5, 14, 6]
[1, 18, 16, 8, 5, 14, 6]
res [18, 8, 16, 1, 5, 14, 6]
res [18, 8, 16, 1, 5, 14, 6]
[18, 8, 16, 1, 5, 14, 6]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
res [1, 5, 16, 8, 12, 14, 6]
[1, 5, 16, 8, 12, 14, 6]
res [1, 12, 16, 8, 5, 14, 6]
[1, 12, 16, 8, 5, 14, 6]
res [16, 12, 14, 8, 5, 1, 6]
res [16, 12, 14, 8, 5, 1, 6]
[16, 12, 14, 8, 5, 1, 6]
>>> extract_heap(arr)
res [14, 12, 6, 8, 5, 1]
res [14, 12, 6, 8, 5, 1]
res [14, 12, 6, 8, 5, 1]
[14, 12, 6, 8, 5, 1]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
res [1, 5, 16, 8, 12, 14, 6]
[1, 5, 16, 8, 12, 14, 6]
res [1, 12, 16, 8, 5, 14, 6]
[1, 12, 16, 8, 5, 14, 6]
res [16, 12, 14, 8, 5, 1, 6]
res [16, 12, 14, 8, 5, 1, 6]
[16, 12, 14, 8, 5, 1, 6]
>>> extract_heap(arr)
res [14, 12, 1, 8, 5, 6]
res [14, 12, 1, 8, 5, 6]
[14, 12, 1, 8, 5, 6]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
res [1, 5, 16, 8, 12, 14, 6]
[1, 5, 16, 8, 12, 14, 6]
res [1, 12, 16, 8, 5, 14, 6]
[1, 12, 16, 8, 5, 14, 6]
res [16, 12, 14, 8, 5, 1, 6]
res [16, 12, 14, 8, 5, 1, 6]
[16, 12, 14, 8, 5, 1, 6]
>>> extract_heap(arr)
res [14, 12, 6, 8, 5, 1]
[14, 12, 6, 8, 5, 1]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
res arr:[1, 5, 16, 8, 12, 14, 6]
arr:[1, 5, 16, 8, 12, 14, 6]
res arr:[1, 12, 16, 8, 5, 14, 6]
arr:[1, 12, 16, 8, 5, 14, 6]
res arr:[16, 12, 14, 8, 5, 1, 6]
res arr:[16, 12, 14, 8, 5, 1, 6]
arr:[16, 12, 14, 8, 5, 1, 6]
>>> extract_heap(arr)
res arr:[14, 12, 6, 8, 5, 1]
[14, 12, 6, 8, 5, 1]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
res max_heapify arr:[1, 5, 16, 8, 12, 14, 6]
build_max_heap [1, 5, 16, 8, 12, 14, 6]
res max_heapify arr:[1, 12, 16, 8, 5, 14, 6]
build_max_heap [1, 12, 16, 8, 5, 14, 6]
res max_heapify arr:[16, 12, 14, 8, 5, 1, 6]
res max_heapify arr:[16, 12, 14, 8, 5, 1, 6]
build_max_heap [16, 12, 14, 8, 5, 1, 6]
>>> extract_heap(arr)
res max_heapify arr:[14, 12, 6, 8, 5, 1]
([14, 12, 6, 8, 5, 1], 16)
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
res None
build_max_heap [1, 5, 16, 8, 12, 14, 6]
res None
build_max_heap [1, 12, 16, 8, 5, 14, 6]
res None
res None
build_max_heap [16, 12, 14, 8, 5, 1, 6]
>>> extract_heap(arr)
res None
([14, 12, 6, 8, 5, 1], 16)
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
build_max_heap [1, 5, 16, 8, 12, 14, 6]
build_max_heap [1, 12, 16, 8, 5, 14, 6]
build_max_heap [16, 12, 14, 8, 5, 1, 6]
>>> extract_heap(arr)
([14, 12, 6, 8, 5, 1], 16)
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
build_max_heap [1, 5, 16, 8, 12, 14, 6]
build_max_heap [1, 12, 16, 8, 5, 14, 6]
build_max_heap [16, 12, 14, 8, 5, 1, 6]
>>> heap_sort(arr)
>>> arr
[]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
build_max_heap [1, 5, 16, 8, 12, 14, 6]
build_max_heap [1, 12, 16, 8, 5, 14, 6]
build_max_heap [16, 12, 14, 8, 5, 1, 6]
>>> heap_sort(arr)
([6, 12, 14, 8, 5, 1], 16)
([1, 12, 14, 8, 5], 6)
([5, 12, 14, 8], 1)
([8, 12, 14], 5)
([14, 12], 8)
([12], 14)
([], 12)
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
build_max_heap [1, 5, 16, 8, 12, 14, 6]
build_max_heap [1, 12, 16, 8, 5, 14, 6]
build_max_heap [16, 12, 14, 8, 5, 1, 6]
>>> heap_sort(arr)
([14, 12, 6, 8, 5, 1], 16)
([12, 8, 6, 1, 5], 14)
([8, 5, 6, 1], 12)
([5, 1, 6], 8)
([6, 1], 5)
([1], 6)
([], 1)
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 5, 6, 8, 12, 14, 16]
>>> build_max_heap(arr)
build_max_heap [1, 5, 16, 8, 12, 14, 6]
build_max_heap [1, 12, 16, 8, 5, 14, 6]
build_max_heap [16, 12, 14, 8, 5, 1, 6]
>>> heap_sort_loop(arr)
>>> arr
[12, 14, 8, 5, 1, 6, 16]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> build_max_heap(arr)
build_max_heap [1, 2, 3, 19, 5, 8, 10, 4]
build_max_heap [1, 2, 10, 19, 5, 8, 3, 4]
build_max_heap [1, 19, 10, 4, 5, 8, 3, 2]
build_max_heap [19, 5, 10, 4, 1, 8, 3, 2]
>>> arr
[19, 5, 10, 4, 1, 8, 3, 2]
>>> extract_heap(arr)
([10, 5, 8, 4, 1, 2, 3], 19)
>>> arr
[10, 5, 8, 4, 1, 2, 3]
>>> extract_heap(arr)
([8, 5, 3, 4, 1, 2], 10)
>>> extract_heap(arr)
([5, 4, 3, 2, 1], 8)
>>> extract_heap(arr)
([4, 1, 3, 2], 5)
>>> extract_heap(arr)
([2, 1, 3], 4)
>>> extract_heap(arr)
([3, 1], 2)
>>> max_heapify([4,1,3,2], 2, 4)
'max_heapify arr:[4, 2, 3, 1]'
>>> extract_heap([5, 4, 3, 2, 1])
([4, 1, 3, 2], 5)
>>> max_heapify([1, 4, 3, 2], 1, 4)
'max_heapify arr:[4, 2, 3, 1]'
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> build_max_heap(arr)
build_max_heap [1, 2, 3, 19, 5, 8, 10, 4]
build_max_heap [1, 2, 10, 19, 5, 8, 3, 4]
build_max_heap [1, 19, 10, 4, 5, 8, 3, 2]
build_max_heap [19, 5, 10, 4, 1, 8, 3, 2]
>>> extract_heap([5, 4, 3, 2, 1])
([4, 2, 3, 1, 1], 5)
>>> extract_heap([4, 2, 3, 1])
([3, 2, 1, 1], 4)

>>> extract_heap([3, 2, 1])
([2, 1, 1], 3)
>>> extract_heap([2, 1])
([1, 1], 2)
>>> extract_heap([1])
([1], 1)
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> extract_heap([5, 4, 3, 2, 1])
([4, 1, 3, 2], 5)
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> extract_heap([5, 4, 3, 2, 1])
([4, 1, 3, 2], 5)
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> extract_heap([5, 4, 3, 2, 1])
[1, 4, 3, 2, 1]
([4, 1, 3, 2], 5)
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> extract_heap([5, 4, 3, 2, 1])
[1, 4, 3, 2, 1]
[1, 4, 3, 2]
([4, 1, 3, 2], 5)
>>> max_heapify([1, 4, 3, 2], 1, 4)
'max_heapify arr:[4, 2, 3, 1]'
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> build_max_heap(arr)
build_max_heap [1, 2, 3, 19, 5, 8, 10, 4]
build_max_heap [1, 2, 10, 19, 5, 8, 3, 4]
build_max_heap [1, 19, 10, 4, 5, 8, 3, 2]
build_max_heap [19, 5, 10, 4, 1, 8, 3, 2]
>>> extract_heap(arr)
([10, 5, 8, 4, 1, 2, 3, 2], 19)
>>> 
>>> 
>>> extract_heap(arr)
([8, 5, 3, 4, 1, 2, 2, 2], 10)
>>> extract_heap(arr)
([5, 4, 3, 2, 1, 2, 2, 2], 8)
>>> extract_heap(arr)
([4, 2, 3, 2, 1, 2, 2, 2], 5)
>>> extract_heap(arr)
([3, 2, 2, 2, 1, 2, 2, 2], 4)
>>> extract_heap(arr)
([2, 2, 2, 2, 1, 2, 2, 2], 3)
>>> extract_heap(arr)
([2, 2, 2, 2, 1, 2, 2, 2], 2)
>>> extract_heap(arr)
([2, 2, 2, 2, 1, 2, 2, 2], 2)
>>> extract_heap(arr)
([2, 2, 2, 2, 1, 2, 2, 2], 2)
>>> len(arr)
8
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> extract_heap([5, 4, 3, 2, 1])
[1, 4, 3, 2, 1]
[1, 4, 3, 2]
([4, 1, 3, 2], 5)
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> extract_heap([5, 4, 3, 2, 1])
[1, 4, 3, 2, 1] 5
[1, 4, 3, 2] 4
([4, 2, 3, 1], 5)
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap_sort(arr)
build_max_heap [1, 2, 3, 19, 5, 8, 10, 4]
build_max_heap [1, 2, 10, 19, 5, 8, 3, 4]
build_max_heap [1, 19, 10, 4, 5, 8, 3, 2]
build_max_heap [19, 5, 10, 4, 1, 8, 3, 2]
[2, 5, 10, 4, 1, 8, 3, 2] 8
[2, 5, 10, 4, 1, 8, 3, 2] 8
heap_sort [10, 5, 8, 4, 1, 2, 3, 2]
[2, 5, 8, 4, 1, 2, 3, 2] 8
[2, 5, 8, 4, 1, 2, 3, 2] 8
heap_sort [8, 5, 3, 4, 1, 2, 2, 2]
[2, 5, 3, 4, 1, 2, 2, 2] 8
[2, 5, 3, 4, 1, 2, 2, 2] 8
heap_sort [5, 4, 3, 2, 1, 2, 2, 2]
[2, 4, 3, 2, 1, 2, 2, 2] 8
[2, 4, 3, 2, 1, 2, 2, 2] 8
heap_sort [4, 2, 3, 2, 1, 2, 2, 2]
[2, 2, 3, 2, 1, 2, 2, 2] 8
[2, 2, 3, 2, 1, 2, 2, 2] 8
heap_sort [3, 2, 2, 2, 1, 2, 2, 2]
[2, 2, 2, 2, 1, 2, 2, 2] 8
[2, 2, 2, 2, 1, 2, 2, 2] 8
heap_sort [2, 2, 2, 2, 1, 2, 2, 2]
[2, 2, 2, 2, 1, 2, 2, 2] 8
[2, 2, 2, 2, 1, 2, 2, 2] 8
heap_sort [2, 2, 2, 2, 1, 2, 2, 2]
[2, 2, 2, 2, 1, 2, 2, 2] 8
[2, 2, 2, 2, 1, 2, 2, 2] 8
heap_sort [2, 2, 2, 2, 1, 2, 2, 2]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap_sort(arr)
build_max_heap [1, 2, 3, 19, 5, 8, 10, 4]
build_max_heap [1, 2, 10, 19, 5, 8, 3, 4]
build_max_heap [1, 19, 10, 4, 5, 8, 3, 2]
build_max_heap [19, 5, 10, 4, 1, 8, 3, 2]
[2, 5, 10, 4, 1, 8, 3, 2] 8
[2, 5, 10, 4, 1, 8, 3] 7
heap_sort [19]
[3, 5, 8, 4, 1, 2, 3] 7
[3, 5, 8, 4, 1, 2] 6
heap_sort [10]
[2, 5, 3, 4, 1, 2] 6
[2, 5, 3, 4, 1] 5
heap_sort [8]
[1, 4, 3, 2, 1] 5
[1, 4, 3, 2] 4
heap_sort [5]
[2, 1, 3, 2] 4
[2, 1, 3] 3
heap_sort [4]
[3, 1, 3] 3
[3, 1] 2
heap_sort [2]
[1, 1] 2
[1] 1
heap_sort [3]
[1] 1
[] 0
heap_sort [1]
>>> array
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    array
NameError: name 'array' is not defined
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap_sort(arr)
build_max_heap [1, 2, 3, 19, 5, 8, 10, 4]
build_max_heap [1, 2, 10, 19, 5, 8, 3, 4]
build_max_heap [1, 19, 10, 4, 5, 8, 3, 2]
build_max_heap [19, 5, 10, 4, 1, 8, 3, 2]
heap_sort [10, 5, 8, 4, 1, 2, 3]
heap_sort [8, 5, 3, 4, 1, 2]
heap_sort [5, 4, 3, 2, 1]
heap_sort [4, 2, 3, 1]
heap_sort [3, 2, 1]
heap_sort [2, 1]
heap_sort [1]
heap_sort []
>>> sorted_array
[19, 10, 8, 5, 4, 3, 2, 1]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap_sort(arr)
build_max_heap [1, 2, 3, 19, 5, 8, 10, 4]
build_max_heap [1, 2, 10, 19, 5, 8, 3, 4]
build_max_heap [1, 19, 10, 4, 5, 8, 3, 2]
build_max_heap [19, 5, 10, 4, 1, 8, 3, 2]
heap_sort [10, 5, 8, 4, 1, 2, 3]
heap_sort [8, 5, 3, 4, 1, 2]
heap_sort [5, 4, 3, 2, 1]
heap_sort [4, 2, 3, 1]
heap_sort [3, 2, 1]
heap_sort [2, 1]
heap_sort [1]
heap_sort []
[19, 10, 8, 5, 4, 3, 2, 1]
>>> 
============== RESTART: D:/SatyamSinha/DS Programs/max_heap.py ==============
>>> arr = [1, 2, 3, 4, 5, 8, 10, 19]
>>> heap_sort(arr)
build_max_heap [1, 2, 3, 19, 5, 8, 10, 4]
build_max_heap [1, 2, 10, 19, 5, 8, 3, 4]
build_max_heap [1, 19, 10, 4, 5, 8, 3, 2]
build_max_heap [19, 5, 10, 4, 1, 8, 3, 2]
heap_sort ([10, 5, 8, 4, 1, 2, 3], 19)
heap_sort ([8, 5, 3, 4, 1, 2], 10)
heap_sort ([5, 4, 3, 2, 1], 8)
heap_sort ([4, 2, 3, 1], 5)
heap_sort ([3, 2, 1], 4)
heap_sort ([2, 1], 3)
heap_sort ([1], 2)
heap_sort ([], 1)
[19, 10, 8, 5, 4, 3, 2, 1]
>>> 
