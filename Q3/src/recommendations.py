"""
Recommendation system based on product ordering patterns.
Analyzing the sequence of the items are being added into the shopping cart to determine which 
products are added next with it
"""

from collections import defaultdict


def analyze_product_sequences(carts):
    """
    Analyze shopping carts to find the most common product that precedes each product.
    
    Args:
        carts (list): List of ShoppingCart objects to analyze
        
    Returns:
        dict: Dictionary mapping product_id to (most_common_predecessor, count)
              Format: {product_id: (predecessor_id, count)}
              where predecessor_id is None if the product is usually added first,
              and count is the number of times this pattern occurs.
              
    Example:
        Given carts with sequences:
        - Cart 1: [A, B, C]
        - Cart 2: [A, B]
        - Cart 3: [A, C]
        - Cart 4: [C, B]
        
        Returns:
        {
            'A': (None, 0),      # A is always first
            'B': ('A', 2),       # B follows A most often (2 times)
            'C': ('A', 2)        # C follows A most often (2 times)
        }
    """
    # Track predecessors: {product_id: {predecessor_id: count}}
    predecessor_counts = defaultdict(lambda: defaultdict(int))
    
    # Tracking products that appear first (no predecessor)
    first_products = defaultdict(int)
    
    # Analyze each cart
    for cart in carts:
        items = cart.get_items()
        
        # Skip empty carts
        if not items:
            continue
        
        # The first item has no predecessor
        first_products[items[0].id] += 1
        
        # record what item came before a specific item
        for i in range(1, len(items)):
            current_product_id = items[i].id
            previous_product_id = items[i - 1].id
            
            # identifying current product which was selected after the previous item
            predecessor_counts[current_product_id][previous_product_id] += 1
    
    # common predecessor for each product
    result = {}
    
    # products whcih were seen as the first item
    for product_id in first_products:
        if product_id not in predecessor_counts:
            result[product_id] = (None, 0)
    
    # finding common products for predecessor product
    for product_id, predecessors in predecessor_counts.items():
        if not predecessors:
            result[product_id] = (None, 0)
        else:
            # Find the predecessor with the highest count
           
            most_common_pred, count = max(predecessors.items(), key=lambda x: x[1])
            result[product_id] = (most_common_pred, count)
    
    return result


def print_recommendation_analysis(analysis):

    print("=" * 70)
    print("PRODUCT SEQUENCE ANALYSIS - RECOMMENDATION")
    print("=" * 70)
    
    if not analysis:
        print("No data to analyze.")
        return
    
    print("\n Ordering Patterns:")
    print("-" * 70)
    
    for product_id, (predecessor, count) in sorted(analysis.items()):
        if predecessor is None:
            print(f"  {product_id}: Added as the first item")
        else:
            print(f"  {product_id}: This item is added after {predecessor} ({count} times)")
    
    print("-" * 70)