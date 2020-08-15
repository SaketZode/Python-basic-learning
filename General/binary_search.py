# incorrect


def get_centre(start, end, length):
    if start > round(length/2):
        return round((end-start)/2) + round((length/2)+1)
    return round((end-start)/2)


global_centre = 0


def binary_search(start_index, end_index, element, elements):
    centre = get_centre(start_index, end_index, len(elements))
    x = globals()['global_centre']
    if x == centre:
        return False, -1
    x = centre
    if elements[centre] == element:
        return True, centre
    if elements[centre] > element:
        return binary_search(start_index, centre-1, element, elements)
    if elements[centre] < element:
        return binary_search(centre+1, end_index, element, elements)
    else:
        return False, -1


lst = [13, 45, 87, 98, 23, 39, 40, 86, 90, 2, 8, 12, 52]
lst.sort()
print(lst)

search = 85

result, ind = binary_search(0, len(lst)-1, search, lst)
if result:
    print("element exist at index ", ind)
else:
    print("does not exist")
