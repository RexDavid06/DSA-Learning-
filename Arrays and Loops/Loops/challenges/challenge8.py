# loop through 1 - 20 but skipp the multiples of 3 and 5

for i in range(21):
    if i % 3 ==0 or  i % 5 == 0:
        continue
    print(i)
