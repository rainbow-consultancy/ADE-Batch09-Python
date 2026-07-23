# name = input("Enter your name: ")
# city = input("now, enter your city name: ")
# print("Good Morning", name)

# print("Hey this is", name, "and I'm from", city)

# formatters

# print("Hey this is {0} and I'm from {1}".format(name, city))
# print("Hey this is {n} and I'm from {c}".format(n=name, c=city))

# print(f"Hey this is {name} and I'm from {city}")


# string default functions

# name = "PYTHONNN"
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.lower().count('n'))

# print(name.endswith("O"))
# print(name.startswith("P"))

# print(name.islower())


# n = "10"
# print(n.isdigit())

# value = "Good,Morning,Students"
# print(value.replace(",", " "))

# nums = "1,2,3,4,5,6"
# nums1 = nums.split(",")
# print(nums1)

# nums = list(map(int, nums.split(",")))
# print(nums)


# nums = list(map(int, nums.split(",")))
# print(nums)

# syntax
# map(para1, para2)

# para1 = function/datatype
# para2 = iterable-datatype (strings, list, tuple)


# filter

# syntax 
# filter(para1:function, para2: iterator)


nums = [1, 2, 3, 4, 5, 6, 7, 8]

# even = []

# for i in nums:
#     if i%2==0:
#         even.append(i)
# print(even)

is_even = lambda x: x%2==0

# def is_even(x):
#     return x%2==0

evens = list(filter(is_even, nums))
print(evens)

evens = list(map(is_even, nums))
print(evens)


# lambda function: Anonymous functions / single line function
# syntax:
#     add = lambda(a, b: a+b)





