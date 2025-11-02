import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.products import Book, MusicAlbum, SoftwareLicense
from src.shopping_cart import ShoppingCart

def test_shopping_cart():
    """============================= Start: Test function to test shopping carts ====================================="""
    print("=" * 60)
    print("========== Shopping Cart Tests  ==========")
    print("=" * 60)
    
    # Create products
    book = Book("B001", "Clean Code", "Robert Martin", 464, 32.99, 0.8)
    album = MusicAlbum("M001", "The Beatles", "Abbey Road", 17, 15.99, 0.1)
    software = SoftwareLicense("S001", "Microsoft Office", 69.99)
    
    # Test 1: Create empty cart
    print("=" * 70)
    print("Testing empty cart function")
    print("=" * 70)
    cart = ShoppingCart()
    print(f"   Items in cart: {cart.get_item_count()}")
    assert cart.get_item_count() == 0, "Cart should be empty"
    print("Successfully completed empty cart testing!")
    
    # Test 2: Add products
    print("=" * 70)
    print("Testing add cart function")
    print("=" * 70)
    cart.add_product(book)
    cart.add_product(album)
    cart.add_product(software)
    print(f"   Items in cart: {cart.get_item_count()}")
    assert cart.get_item_count() == 3, "Confirming cart have three items"
    print("Add products test passed!")
    
    # Test 3: Calculate totals
    print("=" * 70)
    print("Price calculation test function")
    print("=" * 70)
    total_price = cart.get_total_price()
    print(f"   Total price: €{total_price:.2f}")
    assert abs(total_price - 118.97) < 0.01, "Total amount is €118.97"
    print(" Price calculation test passed!")
    

    print("=" * 70)
    print("Weight calculation test function")
    print("=" * 70)
    total_weight = cart.get_total_weight()
    print(f"   Total weight: {total_weight:.2f}kg")
    assert abs(total_weight - 0.9) < 0.01, "Total weight is 0.9kg"
    print(" Weight calculation test passed!")
    
    # Test 4: Remove product
    print("=" * 70)
    print("Remove product test function")
    print("=" * 70)
    removed = cart.remove_product("M001")
    print(f"   Removed album: {removed}")
    print(f"   Items in cart: {cart.get_item_count()}")
    assert removed == True, "album should be removed"
    assert cart.get_item_count() == 2, "cart has two items"
    print("Remove product test passed!")
    
    # Test 5: Try to remove non-existent product
    
    print("=" * 70)
    print("Remove non-existing product test function")
    print("=" * 70)
    removed = cart.remove_product("X999")
    print(f"   Removed: {removed}")
    assert removed == False, "Should return False for non-existent product"
    print(" Non-existent product test passed!")
    
    # Test 6: Display cart
    print("=" * 70)
    print("Cart display test")
    print("=" * 70)
    print(cart)
    
    print("\n" + "=" * 60)
    print("Completed shopping cart tests successfully")
    print("=" * 60)
    
    

if __name__ == "__main__":
    test_shopping_cart()