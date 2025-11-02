"""
Implementing shopping cart for the online store: 
"""

class ShoppingCart:
    def __init__(self):
        """ Initializing a shopping cart """
        
        # store products in a list
        self.items = []
        
    
    def add_product(self, product):
        
        """ 
        function to add a product to cart 
        
        Args:
            product: product to add from given selection (Book, MusicAlbum, or SoftwareLicense)
        
        """
        self.items.append(product) # adding items into the list
        
    def remove_product(self, productid):
        """
        Remove a product from the cart by product_id.
        
        Args:
            product_id (str): selected product id to remove the item from the cart
            
        Returns:
            bool: 
                True -> if product was removed 
                False -> if product not found
        """
        # loop through the item with index
        for i, item in enumerate(self.items):
            # check if item id match
            if item.id==productid:
                self.items.pop(i)
                return True
            
        return False
       
    
    def get_total_price(self):
        """
        Calculate the total price of all items in the cart.
        
        Returns:
            float: Total price in euros
        """
        total = 0
        for item in self.items:
            total +=item.price
            
        return total
    
    
    def get_total_weight(self):
        """
        Calculate the total weight of all items in the cart.
        
        Returns:
            float: Total weight in kilograms
        """
        return sum(item.get_weight() for item in self.items)
        
    
    def get_item_count(self):
        """
        Retrieve number of items in the cart.
        
        Returns:
            int: Number of items
        """
        return len(self.items)

    def clear(self):
        """Remove items from the cart."""
        self.items.clear()


    def get_items(self):
        """
        retrieve items form the cart.
        
        Returns:
            list: Copy of items list
        """
        return self.items
    
    def __str__(self):
        """Return a string  record of the items in the cart."""
        if not self.items:
            return "ShoppingCart(empty)"
        
        items_str = "\n  ".join(str(item) for item in self.items)
        return (f"ShoppingCart(\n  {items_str}\n"
                f"  Total: €{self.get_total_price():.2f}, "
                f"Weight: {self.get_total_weight():.2f}kg)")