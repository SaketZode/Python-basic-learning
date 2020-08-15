def selection_sort(lst):
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]


elements = [45, 95, 12, 32, 21, 78, 56, 54, 102, 259, 99, 33]
selection_sort(elements)
print(elements)
