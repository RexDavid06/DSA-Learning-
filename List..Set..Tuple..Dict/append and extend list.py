x = [1, 5, 6, 7]
y = [90,  45, 56]

x.append(900)
print(x)

x.extend(y)
print(x)

x.insert(4, 500)
print(x)

x.pop()
print(x)

'''the remove function removes the first instance of an item, if we  have multiple 3s in a list, the searches 
and removes the very first instance of the 3'''
x.remove(90)
print(x)

x.sort(reverse=True)
print(x)