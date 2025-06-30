cart = []

def add_item(item):
    cart.append(item)
    print(f"✅ '{item}' added to cart.")

def remove_item(item):
    if item in cart:
        cart.remove(item)
        print(f"❌ '{item}' removed from cart.")
    else:
        print(f"⚠️ '{item}' not found in cart.")

def view_cart():
    if cart:
        print("\n🛒 Cart contents:")
        for i, item in enumerate(cart, 1):
            print(f"{i}. {item}")
        unique_items = set(cart)
        print(f"🧺 Total items: {len(cart)}")
        print(f"🔁 Unique items: {len(unique_items)} → {unique_items}\n")
    else:
        print("🛒 Cart is empty.\n")

def clear_cart():
    cart.clear()
    print("🧹 Cart has been cleared.\n")

# Main loop
print("Welcome to the shopping cart")
while True:
    print("\n1. Add item")
    print("2. Remove item")
    print("3. View cart")
    print("4. Clear cart")
    print("5. Exit")
    
    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("❌ Invalid input. Please enter a number from 1 to 5.")
        continue

    if choice == 1:
        item = input("Enter item to add: ")
        add_item(item)
    elif choice == 2:
        item = input("Enter item to remove: ")
        remove_item(item)
    elif choice == 3:
        view_cart()
    elif choice == 4:
        clear_cart()
    elif choice == 5:
        print("👋 Thanks for using the shopping cart!")
        break
    else:
        print("❌ Invalid choice. Please enter a number from 1 to 5.")
