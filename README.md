# library_management
library management system# Library Management System

## Overview
This is a simple Library Management System built using Python.  
It demonstrates basic Object-Oriented Programming (OOP) concepts such as classes and object relationships.

The system manages:
- Library members
- Books in the library
- Book issue and return transactions

---

## Features

### 1. Library Member Management
- Stores member details like name, email, and phone number.

### 2. Book Management
- Stores book details such as title, author, and total copies.
- Tracks available copies dynamically.

### 3. Book Transactions
- Issue books to members
- Return books from members
- Automatically updates available book copies

---

## System Workflow

1. A member is created.
2. A book is added to the system.
3. The member can issue a book if copies are available.
4. When a book is issued, available copies decrease by 1.
5. When a book is returned, available copies increase by 1.

---

## How to Run

1. Open terminal in the project folder.
2. Run the test file:

```bash
python test_library.py
