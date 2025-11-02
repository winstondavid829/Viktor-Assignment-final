import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

# Import and run your tests
if __name__ == "__main__":
    print("Running all tests...\n")
    
    # Import test files
    from tests import test_products, test_cart
    
    test_products.test_products()
    test_cart.test_shopping_cart()
    
    print("\n All tests completed!")