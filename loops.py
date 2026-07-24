# loops 

# for & while

# for loop

# syntax - 

# for i in range(start: stop: step):
# for i in str, list, dict, tuple:


for i in range(1, 51, 2):
    print(i)

name = "Python"
nums = [1, 2, 3, 4, 5]

for ch in nums:
    print(ch)
    

for i in range(51):
    print(i)


# while loop

# syntax -

# while condition:

i = 1
while i < 51:
    print(i)
    i = i+1
    

# list comprehension

# --> print even numbers between 1 to 30 and append in a list

even = []
for i in range(1, 31):
    if i % 2 == 0:
        even.append(i)
print(even)

even = [i for i in range(1, 31) if i % 2 == 0]
print(even)
