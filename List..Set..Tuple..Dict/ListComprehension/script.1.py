
# nums = [1, 2, 3]
# new_list = [num * 2 for num in nums]
# print(new_list)

# 'Using functions in List Comprehension'
# def timesFive(num:int) -> int:
#     return num * 5


# numbers = [1, 2, 3, 4, 5, 6, 7, 9, 10]
# new_list = [timesFive(number) for number in numbers]
# print(new_list)

'Working with a list of dictionaries'
dicts = [{'name': 'john'}, {'name': 'matthew'}]
results = [i['name'] + ' python' for i in dicts]

print(results)


