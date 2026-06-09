# List comprehension enables you to create a new listg of values using a comprehension or basically a for loop inside a list

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