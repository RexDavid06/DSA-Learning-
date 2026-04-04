items = 'python'

for i in items:
    print(f"{i}")


scores = [80, 50, 60, 75]
total = 0
for score  in scores:
    total = total + score
    print(total)

print(f"Total Value: {total}")


files = [' Report.csv ', ' DATA.csv ', ' final.TXT ']

for  file in files: #this line of code iterates over the variable "files"
    file = file.strip().lower().replace('.txt', '.csv') # the strip method removes the whitespaces,  the .lower  method converts everything to lower case and the .replace  method replacse  the txt to csv
    print(f'Processing {file}')
