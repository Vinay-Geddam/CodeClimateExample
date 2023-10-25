#Code Smells Example for long method
def calculate_item_price(item):
    if item.quantity <= 0:
        return 0
    price = item.price
    if price > 100:
        return price * 0.9
    else:
        return price * 0.95
    
def calculate_total_price(items):
    total = 0
    for item in items:
        total += calculate_item_price(item)
    return total
    
