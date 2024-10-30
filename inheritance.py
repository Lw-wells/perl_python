#library management system

class Book:
    def __init__(self, title, author, ):
        self.title = title
        self.author = author

        def displayinfo():
            return f"Title:{self.title}, Author:{self.author}"

#child class/derived class
class LibraryBook(Book):
    def __init__(self, title, author,isbn,copies_available):
        super().__init__(title, author)
        self.isbn = isbn
        self.copies_available = copies_available
    def borrow_book(self):
        if self.copies_available >0:
            self.copies_available -= 1
            return f"{self.title} borrowed.copies left {self.copies_available}"
        else:
            return f"No of Title {self.titel} available"
    def return_book(self):
        self.copies_available += 1
        return f"{self.title} returned.copies left {self.copies_available}"

#usage example
book1=LibraryBook("Blossoms","Maina Kinani", 475858, 18)
print(book1.borrow_book())
print(book1.return_book())
