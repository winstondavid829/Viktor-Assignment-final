import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.products import Book, MusicAlbum, SoftwareLicense


def test_products():
    print(f"================= Product test: Start ==================")
    # Create a book
    book = Book("B001", "Clean Code", "Robert Martin", 464, 32.99, 0.8)
    print(book)
    print(f"Weight: {book.get_weight()}kg")
    print()

    # Create a music album
    album = MusicAlbum("M001", "The Beatles", "Abbey Road", 17, 15.99, 0.1)
    print(album)
    print(f"Weight: {album.get_weight()}kg")
    print()

    # Create a software license
    software = SoftwareLicense("S001", "Microsoft Office", 69.99)
    print(software)
    print(f"Weight: {software.get_weight()}kg")
    print()

    print("Successfully created product records!!")

    print(f"================= Product test: End ==================")
    
if __name__ == "__main__":
    test_products()