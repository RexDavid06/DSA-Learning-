x = {
    'name': 'mona',
    'age' : 29,
    'nationality': 'nigerian'
}

y = dict(name='jude', age=20, nationality='nigerian')

z = dict([('name', 'mark'), ('age', 40), ('nationality', 'polish')])

# print(type(x))
# #adds or modifies a key-value pair in thje dict
# x['nationality'] = 'spanish'
# x['NIN'] = 567489304
# del(x['NIN'])
# print(x)
# print(len(x))
# # checking membership
# print('mona' in x.values())
# x.clear()
# print(x)




print(type(y))
print(y)

#iterating over a dictionary
for key, value in y.items():
    print(key, value)

# print(type(z))
# print(z)