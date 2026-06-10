# So, i will use the traditional approcah first then the List Comprehension Approach

# 1. Create a list of squares from 1 to 10
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
square_list = []
'''Traditional Approach'''
for item in x:
    items = item ** 2 # OR pow(item, 2)
    square_list.append(items)

print(square_list)

'''List Comprehension Approach'''
square_list2 = [pow(item, 2) for item in x]
print(square_list2)


# 2. Create a list of even numbers from 1 to 20
even_numbers = []
'''Traditional Approach'''
for item in range(21):
    if item % 2 == 0:
        even_numbers.append(item)
print(even_numbers)

'''List Comprehension Approach'''
even_numbers2 = [item for item in range(21) if item % 2 == 0]
print(even_numbers2)


# 3. Given the list below, use list comprehension to convert all the names to UPPERCASE
names = ['rex', 'john', 'mary', 'jane']
new_list = []
'''Traditional Approach'''
for item in names:
    items = item.upper()
    new_list.append(items)

print(new_list)

'''List Comprehension Approach'''
new_list = [item.upper() for item in names]
print(new_list)


# 4. Given the list below, create a new list containing only the numbers greater than 10
x = [2, 5, 8, 11, 14, 17]
new_list = []

'''Traditional Approach'''
for item in x:
    if item > 10:
        new_list.append(item)

print(new_list)

'''List Comprehension Approach'''

new_list = [item for item in x if item > 10]
print(new_list)