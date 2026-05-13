


from library_system import Member, Book, Transaction

# Create members
m1 = Member("Nikita", "nikita@mail.com", "1234567890")

# Create books
b1 = Book("Python Basics", "Guido van Rossum", 2)

# Transaction system
t = Transaction()

# Issue book
t.issue_book(m1, b1)
print("Available copies:", b1.available_copies)

# Return book
t.return_book(m1, b1)
print("Available copies:", b1.available_copies)        


