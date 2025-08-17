import json
from product import Product


def product_exists(name, products):
    for product in products:
        if product.name.lower() == name.lower():
            return product
    return None

def checkout(cart):
    total = 0
    for name, quantity, price in cart:
        subtotal = quantity * price
        total += subtotal
        print(f"{name}: {quantity} x {price} = {subtotal:.02f}€")
    return total

def save_products(filename, products):
    data = [product.to_dict() for product in products]
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_products(filename):
    with open(filename, "r") as file:
        data = json.load(file)

    return [Product.from_dict(item) for item in data]


def main():
    try:
        products = load_products("products.json")
    except FileNotFoundError:
        products = [
            Product("Apple", 0.5, 20),
            Product("Milk", 1.2, 10),
            Product("Banana", 1, 12),
            Product("Bread", 0.8, 25),
            Product("Chicken", 6, 8),
            Product("Juice", 1.5, 10)
        ]


    cart = []
    print("Welcome to the store.")

    while True:
        print("The products are: ")
        for product in products:
            print(product)

        product_name = input("Enter the name of the product you want: ")
        product_obj = product_exists(product_name, products)
        if product_obj:
            while True:
                quantity = input("Select the quantity you want: ")
                try:
                    quantity = float(quantity)
                    if quantity > 0:
                        break
                    else:
                        print("Quantity must be greater than zero.")
                except ValueError:
                    print("Wrong input. Enter a number: ")

            if quantity <= product_obj.quantity:
                product_obj.quantity -= quantity
                print(f"{quantity} of {product_obj.name} added to cart.")
                cart.append((product_obj.name, quantity, product_obj.price))
            else:
                print("Not enough quantity.")
        else:
            print(f"The product '{product_name}' doesn' t exist.")

        another = input("Do you want to buy another product? (yes/no): ").lower()
        if another != "yes":
            print("Thank you for shopping!")
            save_products("products.json", products)
            break

    total = checkout(cart)
    print(f"Total: {total:.02f}€")

if __name__ == "__main__":
        main()
