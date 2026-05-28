#Find two numbers that add up to target
numbers = [2, 7, 11, 15]
target = 9

def two_sums(numbers, target):
    seen = {}

    for index, num in enumerate(numbers):
        diff = target - num
        
        if diff in seen:
            return [seen[diff], index]