# f = open('text.txt', 'r')

# print(f.name)
# print(f.mode)

# f.close()

# Using context manager
# with open('text.txt', 'r') as f:
#     size_read = 100
#     f_content = f.read(size_read)
#     print(f_content)

# with open('text2.txt', 'w') as f:
#     f.write('New Text File for learning')


# 'Copy information from one file to another'
# with open('text.txt', 'r') as rf:
#     with open('text2.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)


# 'Using binary mode for copying from non-txt files'
# with open('contacts.csv', 'rb') as rf:
#     with open('text2.txt', 'wb') as wf:
#         for line in rf:
#             wf.write(line)


with open('contacts.csv', 'rb') as rf:
    rf_contents = rf.read()
    print(rf_contents)