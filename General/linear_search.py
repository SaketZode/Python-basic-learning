def search_element(element, elements):
    status = False
    for i in range(0, len(elements)):
        if elements[i] == element:
            status = True
            break
    return status, i


lst = [13, 45, 87, 98, 23, 39, 40, 86, 90, 2, 8, 12]

search = int(input("Enter element to search : "))

result, ind = search_element(search, lst)
if result:
    print("element exist at index ", ind)
else:
    print("does not exist")


"""
OR
"""


if search in lst:
    print("exist at index ", lst.index(search))
else:
    print("No")
