import datetime

class BillItem:
    def __init__(self, product_name, price, quantity, discount=0):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.discount = discount

    def calculate_total_cost(self):
        total_cost = self.price * self.quantity
        if self.discount > 0:
            total_discount = (total_cost * self.discount) / 100
            total_cost -= total_discount
        return total_cost

    def generate_item_bill(self):
        total_cost = self.calculate_total_cost()
        item_output = f"Product Name: {self.product_name}\n"
        item_output += f"Quantity: {self.quantity}\n"
        item_output += f"Price per Unit: ${self.price:.2f}\n"
        item_output += f"Total Cost: ${total_cost:.2f}\n"
        if self.discount > 0:
            item_output += f"Discount: {self.discount}%\n"
        return item_output


def get_float_input(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_int_input(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def main():
    items = []
    while True:
        product_name = input("Enter product name (or 'done' to finish): ")
        if product_name.lower() == "done":
            break

        price = get_float_input("Enter price per unit: ")
        quantity = get_int_input("Enter quantity: ")
        discount = get_float_input("Enter discount percentage (if applicable): ")

        item = BillItem(product_name, price, quantity, discount)
        items.append(item)

    print("\n----- Bill -----\n")
    total_cost = 0
    for item in items:
        item_bill = item.generate_item_bill()
        print(item_bill)
        total_cost += item.calculate_total_cost()

    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\nTotal Cost for all items: ${total_cost:.2f}")
    print(f"Date and Time: {current_date_time}")


if __name__ == "__main__":
    main()
