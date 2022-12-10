from models.book import *


book1 = Book("The Hunger Games", "Suzanne Collins", "Adventure", "The Hunger Games is a 2008 dystopian novel by the American writer Suzanne Collins. It is written in the perspective of 16-year-old Katniss Everdeen, who lives in the future, post-apocalyptic nation of Panem in North America")
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy", "Harry Potter, an eleven-year-old orphan, discovers that he is a wizard and is invited to study at Hogwarts. Even as he escapes a dreary life and enters a world of magic, he finds trouble awaiting him")
book3 = Book("To Kill a Mockingbird", "Harper Lee","Southern Gothic", "To Kill a Mockingbird is a novel by the American author Harper Lee. It was published in 1960 and was instantly successful. In the United States, it is widely read in high schools and middle schools. To Kill a Mockingbird has become a classic of modern American literature, winning the Pulitzer Prize.")
book4 = Book("The Alchemist", "Paulo Coelho", "Adventure", "The Alchemist is a novel by Brazilian author Paulo Coelho which was first published in 1988. Originally written in Portuguese, it became a widely translated international bestseller")
book5 = Book("The School for Gods", "Stefano D'anna", "Fiction", "This book is a map and an escape plan. In The School of Gods, Stefano Elio D'anna reveals the path taken by ordinary men to escape the rut of a programmed destiny. A path removed from an hypnotic view of the world and an accusing and plaintive interpretation of existence.")
book6 = Book("Think and Grow Rich", "Napoleon Hill", "Non-Fiction", "Think and Grow Rich is a book written by Napoleon Hill in 1937 and promoted as a personal development and self-improvement book. He claimed to be inspired by a suggestion from business magnate and later-philanthropist Andrew Carnegie")

books = [book1, book2, book3, book4]


def add_new_book(book):
    books.append(book)

def delete_book_at_index(index):
    books.pop(index)