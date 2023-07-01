menu = []
orders = []

# Add a new dish to the menu
def add_dish_to_menu():
    dish_id = int(input("Enter the dish ID: "))
    dish_name = input("Enter the dish name: ")
    price = float(input("Enter the price: "))
    availability = input("Enter the availability (yes/no): ")

    dish = {
        "dish_id": dish_id,
        "dish_name": dish_name,
        "price": price,
        "availability": availability.lower()
    }

    menu.append(dish)
    print(f"Dish '{dish_name}' added to the menu.")

# Remove a dish from the menu
def remove_dish_from_menu():
    dish_id = int(input("Enter the dish ID to remove: "))

    for dish in menu:
        if dish["dish_id"] == dish_id:
            menu.remove(dish)
            print(f"Dish with ID '{dish_id}' removed from the menu.")
            return

    print(f"Dish with ID '{dish_id}' not found in the menu.")

# Update the availability of a dish
def update_dish_availability():
    dish_id = int(input("Enter the dish ID to update availability: "))
    availability = input("Enter the new availability (yes/no): ")

    for dish in menu:
        if dish["dish_id"] == dish_id:
            dish["availability"] = availability.lower()
            print(f"Availability of dish with ID '{dish_id}' updated.")
            return

    print(f"Dish with ID '{dish_id}' not found in the menu.")

# Display the menu
def display_menu():
    if len(menu) == 0:
        print("Menu is empty.")
    else:
        print("Menu:")
        print("{:<10} {:<20} {:<10} {:<12}".format("Dish ID", "Dish Name", "Price", "Availability"))
        for dish in menu:
            print("{:<10} {:<20} {:<10} {:<12}".format(dish["dish_id"], dish["dish_name"], dish["price"], dish["availability"]))

# Take a new order
def take_order():
    customer_name = input("Enter customer name: ")

    # Display the menu with available dishes
    available_menu = [dish for dish in menu if dish["availability"] == "yes"]
    print("Available Menu:")
    print("{:<10} {:<20} {:<10}".format("Dish ID", "Dish Name", "Price"))
    for dish in available_menu:
        print("{:<10} {:<20} {:<10}".format(dish["dish_id"], dish["dish_name"], dish["price"]))

    order_items = []
    while True:
        dish_id = int(input("Enter dish ID (0 to finish order): "))
        if dish_id == 0:
            break

        dish = next((d for d in available_menu if d["dish_id"] == dish_id), None)
        if dish:
            quantity = int(input("Enter quantity: "))
            order_items.append({
                "dish_id": dish_id,
                "dish_name": dish["dish_name"],
                "quantity": quantity,
                "price": dish["price"]
            })
        else:
            print("Invalid dish ID. Please try again.")

    if len(order_items) > 0:
        order_id = len(orders) + 1
        order = {
            "order_id": order_id,
            "customer_name": customer_name,
            "items": order_items,
            "status": "received"
        }
        orders.append(order)
        print(f"Order with ID '{order_id}' placed successfully.")
    else:
        print("No items selected for the order.")

# Update the status of an order
def update_order_status():
    order_id = int(input("Enter order ID: "))
    status = input("Enter the new status: ")

    order = next((o for o in orders if o["order_id"] == order_id), None)
    if order:
        order["status"] = status
        print(f"Status of order with ID '{order_id}' updated.")
    else:
        print(f"Order with ID '{order_id}' not found.")

# Display all orders or filter by status
def display_orders():
    status_filter = input("Enter the status to filter (leave empty for all orders): ")

    if len(orders) == 0:
        print("No orders found.")
    else:
        if status_filter:
            filtered_orders = [order for order in orders if order["status"].lower() == status_filter.lower()]
        else:
            filtered_orders = orders

        if len(filtered_orders) == 0:
            print("No orders found with the specified status.")
        else:
            print("Orders:")
            for order in filtered_orders:
                print(f"Order ID: {order['order_id']}")
                print(f"Customer Name: {order['customer_name']}")
                print("Items:")
                for item in order["items"]:
                    print(f"- {item['dish_name']}, Quantity: {item['quantity']}, Price: {item['price']}")
                print(f"Status: {order['status']}")
                print()

# Main program
while True:
    print("\n=== Zomato Chronicles: The Great Food Fiasco ===")
    print("1. Add Dish to Menu")
    print("2. Remove Dish from Menu")
    print("3. Update Dish Availability")
    print("4. Display Menu")
    print("5. Take New Order")
    print("6. Update Order Status")
    print("7. Display Orders")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")

    if choice == '1':
        add_dish_to_menu()
    elif choice == '2':
        remove_dish_from_menu()
    elif choice == '3':
        update_dish_availability()
    elif choice == '4':
        display_menu()
    elif choice == '5':
        take_order()
    elif choice == '6':
        update_order_status()
    elif choice == '7':
        display_orders()
    elif choice == '8':
        print("Thank you for using Zomato Chronicles: The Great Food Fiasco!")
        break
    else:
        print("Invalid choice. Please try again.")
