# List comprehension enables you to create a new list of values using a comprehension or basically a for loop inside a list

# Traditional Approach
names = ['Yola', 'Micheal', 'James', 'Yankee', 'Jude', 'Yando']
y_name = []

for items in names:
    if 'Y' in items:
        y_name.append(items)

print(y_name)

#List Comprehension Approach
y_name = [item for item in names if 'Y' in item]
print(y_name)


# Getting the multiples of 10 with there indexes!
'''Traditional Approach'''
y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for index, item in enumerate(y):
    multiple = item * 10
    print(index, multiple)


# Getting all numbers from a string
s = '1 love t0 g0 swimmin9 in 7he morning2'

'''Traditional Approach'''
nums = []
for item in s:
    if item.isnumeric():
        nums.append(item)

print(nums)

'''List Comprehension Approach'''
nums = [item for item in s if item.isnumeric()]
print(nums)
        

# Getting the Index of a specific item in the list
names = ['Cosmo', 'Pedro', 'Anu', 'Ray']
'''Traditional Approach'''
for index, item in enumerate(names):
    if item == 'Anu':
        print('Index: '+ str(index))


'''List Comprehension Approach'''
x = [(index) for index, item in enumerate(names) if item == 'Cosmo']
print(f'Index: {x[0]}')

# Using If Else in List Comprehension..

words = 'The lord 1s  M1racle G0d'
alpha = []
numeric = [item if item.isnumeric() else alpha.append(item) for item in words]


print(numeric)

# Nested loop iteration for 2D list
a = [[1,2], [3,4]]

''' Traditional Approach'''
new_list = []

'''iterating over the lists in a and storing it in i '''
for i in a:
    ''' iterating over the stored list in i to get individaul elements inside of i'''
    for item in i:
        new_list.append(item)
print(new_list)

'''List Comprehension Approach'''
new_list = [item for i in a for item in i] # I feel fucking Amazed right now!!
print(new_list)       
