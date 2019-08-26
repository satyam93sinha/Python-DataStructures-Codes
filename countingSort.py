def counting_sort(ar):
    min_arr = min(ar)
    max_arr = max(ar)
    list_, counting, count = [], [], []
    for i in range(min_arr, max_arr+1):
        list_.append(i)
        counting.append(ar.count(i))
    for j in range(len(list_)):
        if counting[j] != 0:
            count.append(list_[j])
    print(count)
    for k in range(len(ar)):
        ar[k] = count[k]
