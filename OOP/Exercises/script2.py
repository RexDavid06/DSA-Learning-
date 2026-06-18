'''
Create a book class 
    Requirements
        Instance Attributes
            Title
            Author
        Class Attributes
            total_books = 0
        
            
Everytime a book is created, increase the total _books by 1
'''

class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1


book1 = Book('48 Laws of Power', 'Robert Greene')
book2 = Book('Revelations', 'John')

print(book1.author)
print(book2.title)
print(Book.total_books)