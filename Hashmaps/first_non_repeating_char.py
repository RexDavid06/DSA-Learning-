# counts = {}

# counts['a'] = 1

# print(counts.get('b', 'b is not a key'))

# if 1 in counts.values():
#     print('it exists in the dict')
# else:
#     print('it does not exists')

s = 'racecarf'

#Find the first non-repeating characters in a string

def get_first_non_repeating_char(s: str):
    counts = {}

    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in s:
        if counts[char] == 1:
            return char
       

print(get_first_non_repeating_char(s))

# I HONESTLY STILL DON'T UNDERSTAND THIS CODE!!
