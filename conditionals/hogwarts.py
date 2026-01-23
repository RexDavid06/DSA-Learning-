# students = ['Hermione', 'Harry', 'Ron']

# for i in range(len(students)):
#     print(i+1, students[i])


hogwart_students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in hogwart_students:
    print(student["name"], student["house"], student["patronus"], sep=", ")


#building a block of hashes
def main():
    print_column(5)


def print_column(n):
    for _ in range(n):
        print("#")

main()   
