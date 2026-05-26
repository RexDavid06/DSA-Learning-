# x = set()
# print(type(x))
# x.add(4)
# print(x)
# print(5 in x)
# x.clear()
# print(x)

s1 = {2, 1, 3}
s2 = {3, 8, 9 }

# INTERSECTION AND (what is in set 1 and set 2)
print(s1 & s2)

#UNION OR (merging the two sets orderly)
print(s1 | s2)

# Symmetric Difference
print(s1 ^ s2)
print(s1 - s2)
print(s1 <= s2) 
print(s1 >= s2)

y = {3, 4, 5}
print(type(y))