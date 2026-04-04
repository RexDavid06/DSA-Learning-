# the break statement is used to immediately  stop the loop   no matter where you are in the loop   and moves next to the next line of code

names = ['john', 'maria', ' ', 'kumar']

# for name in names:
#     if name == ' ':
#         print('Empty vaue detected')
#         break
#     print(f'name = {name}')


#the continue statement is used to skip  one loop circle
# we can use continue to skip  bad or empty data without stopping the whole  loop

for name in names:
    if name == ' ':
        print('Empty vaue detected')
        continue
    print(f'name = {name}')


# the pass statement is a  place holder where nothing happens....

for name in names:
    if name == ' ':
        pass #todo: Handle   Empty Value
    print(f'name = {name}')

