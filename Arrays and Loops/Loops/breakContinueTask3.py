# Check  for even number

items = [1,  3,  4, 7]

for i in items:
    if i %  2 == 0:
        print("Even Nr  found: ", i)
        break
else:
    print('All numbers are odd')