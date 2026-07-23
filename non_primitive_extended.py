# list | tuple | set | dict

nums = [1, 2, 3, 4, 5]
nums2 = [30, 20, 10]

# append - used to add values at the end of the list
# nums.append(6)
# print(nums)

# pop - used to remove/delete value at the end of the list
# nums.pop()
# print(nums)

# remove - used to remove/delete value in the list which user has specified 
# nums.remove(3)
# print(nums)

# count - used to count an item occurance in the list
# print(nums.count(5))

# len - used to find the legth/total no.of items present in the list
# print(len(nums))

# sort - used to sort the items in the list either in asc/desc order
# nums.sort()
# print(nums)

# nums.sort(reverse=True)
# print(nums)

# way to replace an item in the list
# nums[2] = 6
# print(nums)

# extend

# nums.extend(nums2)
# print(nums)


# tuple - immutable

nums = (1, 2, 3, 4, 5)

# print(len(nums))

# print(nums.count(3))

# print(nums.index(5))

# throws error
# nums[2] = 6
# print(nums)


# set - mutable

my_set = {1, 2, 3, 4, 3, 5, 6, 7}
my_set2 = {11, 12, 30, 24}
# print(my_set)

# add - add new items to the set 
# my_set.add(10)
# print(my_set)

# print(my_set.union(my_set2))


# dictionaries - dict

stu_info = {
    "id": 100,
    "name": "Prathap",
    "city": "Bangalore"
}

# add a new item into the dict
stu_info["country"] = "India"
print(stu_info)

# modify the value
stu_info["city"] = "Hyderabad"
print(stu_info)

print(stu_info["name"])
print(stu_info.get("name"))

# stu_info.pop("country")
# print(stu_info)

stu_info.popitem()
print(stu_info)

print(stu_info.keys())
print(stu_info.values())
