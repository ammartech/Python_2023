import datetime

# Predefined list of available food items with prices
food_items = {
    "pizza": 10.99,
    "burger": 5.99,
    "fries": 2.99,
    "coke": 1.99
}

# List to store all orders
orders = []

def run():
    global FOOD_ITEMS
    FOOD_ITEMS = []
    """Function to run the food ordering system"""
    while True:
        print("\nWelcome to the Food Ordering System!\n")
        print("Please select an option:")
        print("1. Add new food items")
        print("2. New order")
        print("3. List all orders")
        print("4. View order")
        print("5. Update order")
        print("6. Cancel order")
        print("7. Save food items list")
        print("8. Save orders")
        print("9. Exit")

        choice = input("\nEnter your choice (1-9): ")
        print()

        if choice == '1':
            add_food_items()
        elif choice == '2':
            new_order()
        elif choice == '3':
            list_orders()
        elif choice == '4':
            view_order()
        elif choice == '5':
            update_order()
        elif choice == '6':
            cancel_order()
        elif choice == '7':
            save_food_items()
        elif choice == '8':
            save_orders()
        elif choice == '9':
            exit_system()
        else:
            print("Invalid choice. Please try again.")


def add_food_items():
    """Function to add a new food item to the predefined list"""
    item_name = input("Enter the name of the food item: ")
    item_price = float(input("Enter the price of the food item: "))
    food_items[item_name] = item_price

def new_order():
    """Function to place a new order"""
    customer_name = input("Enter the customer name: ")
    customer_mobile_number = input("Enter the customer mobile number: ")
    order_date = datetime.date.today().strftime("%Y-%m-%d")
    order_items = []
    total_amount = 0

    # Loop to select food items and their quantities for the order
    while True:
        print("Available food items:")
        for item_name, item_price in food_items.items():
            print(f"{item_name} - ${item_price}")
        item_name = input("Enter the name of the food item (press 'q' to finish): ")
        if item_name == 'q':
            break
        elif item_name not in food_items:
            print("Invalid food item!")
            continue
        item_quantity = int(input("Enter the quantity of the food item: "))
        order_items.append({"name": item_name, "price": food_items[item_name], "quantity": item_quantity})
        total_amount += food_items[item_name] * item_quantity
    
    # Add the new order to the orders list
    orders.append({
        "customer_name": customer_name,
        "customer_mobile_number": customer_mobile_number,
        "order_date": order_date,
        "order_items": order_items,
        "order_status": "new",
        "total_amount": total_amount
    })
    print("Order placed successfully!")

def list_orders():
    """Function to list all orders"""
    print("All orders:")
    for order in orders:
        print(f"Customer Mobile Number: {order['customer_mobile_number']}, Customer Name: {order['customer_name']}, Order Date: {order['order_date']}, Final Amount: ${order['total_amount']}, Order Status: {order['order_status']}")

def view_order():
    """Function to view the details of a specific order"""
    customer_mobile_number = input("Enter the customer mobile number to search for the order: ")
    for order in orders:
        if order['customer_mobile_number'] == customer_mobile_number:
            print(f"Customer Name: {order['customer_name']}, Customer Mobile Number: {order['customer_mobile_number']}, Order Date: {order['order_date']}, Order Status: {order['order_status']}, Total Amount: ${order['total_amount']}")
            print("Order Items:")
            for item in order['order_items']:
                print(f"{item['name']} - ${item['price']} x {item['quantity']}")
            return
    print("Order not found!")

def update_order():
    """Function to update the status of a specific order"""
    customer_mobile_number = input("Enter the customer mobile number to search for the order: ")
    for order in orders:
        if order['customer_mobile_number'] == customer_mobile_number:
            new_status = input("Enter the new status of the order: ")
            order['order_status'] = new_status
            print("Order status updated successfully!")
            break
    else:
        print("No order found with the given mobile number.")
def cancel_order():
    """Function to cancel a specific order"""
    customer_mobile_number = input("Enter the customer mobile number to search for the order: ")
    for order in orders:
        if order['customer_mobile_number'] == customer_mobile_number:
            order['order_status'] = 'canceled'
            print("Order canceled successfully!")
            break
    else:
        print("No order found with the given mobile number.")


FOOD_FILE = "food_items.txt"

def save_food_items():
    with open(FOOD_FILE, "w") as f:
        for item in FOOD_ITEMS:
            f.write(f"{item}\n")
    print("Food items list saved successfully!")

def save_orders():
    """Function to save the orders list to a file"""
    with open('orders.txt', 'w') as f:
        for order in orders:
            f.write(str(order) + "\n")
    print("Orders saved successfully!")


def exit_system():
    """Function to exit the system"""
    print("Exiting the food ordering system. Thank you for using our service!")
    exit()

run()
