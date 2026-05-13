class Member:
    def __init__(self, name, email="", phone=""):
        self.name = name
        self.email = email
        self.phone = phone


class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies


class Transaction:
    def __init__(self):
        self.records = []

    def issue_book(self, member, book):
        if book.available_copies > 0:
            book.available_copies -= 1
            self.records.append({
                "member": member.name,
                "book": book.title,
                "status": "Issued"
            })
            print(f"{member.name} issued {book.title}")
        else:
            print("Book not available")

    def return_book(self, member, book):
        book.available_copies += 1
        self.records.append({
            "member": member.name,
            "book": book.title,
            "status": "Returned"
        })
        print(f"{member.name} returned {book.title}")
