stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    total_items = 0
    print("Inventory:")
    
    for item,total in inventory.items():
        total_items = total_items + total
        print(total, item)
    
    print("Total number of items:", total_items)

if __name__ == "__main__":
    displayInventory(stuff)
