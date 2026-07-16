def topTen():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values = topTen()
print(values)
# print(next(values))
# print(values.__next__())

for i in values:
    print(i)