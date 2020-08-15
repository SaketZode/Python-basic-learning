def bubble_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


elements = [45, 95, 12, 32, 21, 78, 56, 54, 102, 259, 99, 33]
bubble_sort(elements)
print(elements)
