# examples/demo.py
"""
Demonstration of the shopping cart system.
Shows all features including product creation, cart operations, calculations,
and the bonus recommendation system.
"""

import sys
import os
# Add parent directory to path so we can import from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.products import Book, MusicAlbum, SoftwareLicense
from src.shopping_cart import ShoppingCart
from src.recommendations import analyze_product_sequences, print_recommendation_analysis


def main():
    """Main function"""
    print("=" * 70)
    print("ONLINE STORE - SHOPPING CART DEMO")
    print("=" * 70)
    
    # Step 1: Create products
    print("\n" + "=" * 70)
    print("STEP 01: Creating Products")
    print("=" * 70)
    
    print("\n BOOKS:")
    book1 = Book("B001", "Clean Code", "Robert C. Martin", 464, 32.99, 0.8)
    print(f"  {book1}")
    
    book2 = Book("B002", "The Pragmatic Programmer", "Andrew Hunt", 352, 34.99, 0.7)
    print(f"  {book2}")
    
    print("\n MUSIC ALBUMS:")
    album1 = MusicAlbum("M001", "The Beatles", "Abbey Road", 17, 15.99, 0.1)
    print(f"  {album1}")
    
    album2 = MusicAlbum("M002", "Pink Floyd", "The Dark Side of the Moon", 10, 14.99, 0.1)
    print(f"  {album2}")
    
    print("\n SOFTWARE:")
    software1 = SoftwareLicense("S001", "Microsoft Office 365", 69.99)
    print(f"  {software1}")
    
    software2 = SoftwareLicense("S002", "Adobe Creative Cloud", 52.99)
    print(f"  {software2}")
    
    # Step 2: Create shopping cart
    print("\n" + "=" * 70)
    print("STEP 02: Shopping Cart Operations")
    print("=" * 70)
    
    cart = ShoppingCart()
    print("\n Created empty shopping cart")
    print(f"Items in cart: {cart.get_item_count()}")
    
    print("\n Adding products to cart...")
    cart.add_product(book1)
    print(f" Added: {book1.title}")
    
    cart.add_product(album1)
    print(f" Added: {album1.title} by {album1.artist}")
    
    cart.add_product(software1)
    print(f" Added: {software1.name}")
    
    cart.add_product(book2)
    print(f" Added: {book2.title}")
    
    print(f"\n Items in cart: {cart.get_item_count()}")
    
    print("\n Current Cart:")
    print(cart)
    
    # Step 3: Detailed Calculations
    print("\n" + "=" * 70)
    print("STEP 3: Price & Weight Calculations")
    print("=" * 70)
    
    print("\n Price Breakdown:")
    for item in cart.get_items():
        print(f"  {item.id}: €{item.price:.2f}")
    print(f"  {'─' * 30}")
    print(f"  TOTAL: €{cart.get_total_price():.2f}")
    
    print("\n Weight Breakdown:")
    for item in cart.get_items():
        weight = item.get_weight()
        weight_str = f"{weight:.2f}kg" if weight > 0 else "0.00kg (digital)"
        print(f"  {item.id}: {weight_str}")
    print(f"  {'─' * 30}")
    print(f"  TOTAL: {cart.get_total_weight():.2f}kg")
    
    # Step 4: Removing Products
    print("\n" + "=" * 70)
    print("STEP 04: Removing Products")
    print("=" * 70)
    
    print("\n Removing 'Abbey Road' from cart...")
    removed = cart.remove_product("M001")
    if removed:
        print(" Successfully removed")
    else:
        print(" Product not found")
    
    print(f"\n Items in cart: {cart.get_item_count()}")
    
    print("\n  Trying to remove non-existent product (ID: X999)...")
    removed = cart.remove_product("X999")
    if removed:
        print("  Successfully removed")
    else:
        print("  Product not found (as expected)")
    
    print("\n Updated Cart:")
    print(cart)
    
    # Step 5: Recommendation System Demo
    print("\n" + "=" * 70)
    print("STEP 5: Recommendation System ")
    print("=" * 70)
    
    print("\n Creating multiple shopping cart scenarios for analysis...")
    
    # Create different cart scenarios
    scenario_cart1 = ShoppingCart()
    scenario_cart1.add_product(book1)
    scenario_cart1.add_product(album1)
    scenario_cart1.add_product(software1)
    
    scenario_cart2 = ShoppingCart()
    scenario_cart2.add_product(book1)
    scenario_cart2.add_product(album1)
    
    scenario_cart3 = ShoppingCart()
    scenario_cart3.add_product(book1)
    scenario_cart3.add_product(software2)
    
    scenario_cart4 = ShoppingCart()
    scenario_cart4.add_product(software1)
    scenario_cart4.add_product(book2)
    
    scenario_cart5 = ShoppingCart()
    scenario_cart5.add_product(album2)
    scenario_cart5.add_product(book2)
    
    scenario_carts = [scenario_cart1, scenario_cart2, scenario_cart3, scenario_cart4, scenario_cart5]
    
    print("\nCart sequences:")
    print("-" * 70)
    for i, sc in enumerate(scenario_carts, 1):
        items = sc.get_items()
        sequence = " → ".join(item.id for item in items)
        print(f"  Cart {i}: {sequence}")
    print("-" * 70)
    
    print("\n Analyzing product ordering patterns...")
    analysis = analyze_product_sequences(scenario_carts)
    
    print()
    print_recommendation_analysis(analysis)
    
    
    
    print("\n" + "=" * 70)
    print("Shopping cart implementation completed")
    print("=" * 70)


if __name__ == "__main__":
    main()