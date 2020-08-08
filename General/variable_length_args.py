def sum(*nums):
    sum = 0
    for i in nums:
        sum += i
    return sum


print(sum(1, 2, 3, 4, 5))
print(sum(45, 67, 23))


def person(name, age, city):
    print("Name : ", name)
    print("Age : ", age)
    print("City : ", city)


person(name='saket', city='Bangalore', age=23)


def human(name, **data):
    print("Name : ", name)
    for i, j in data.items():
        print(i, j)


human('saket', age=23, city='bangalore')
