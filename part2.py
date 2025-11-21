
import time



class Goods:
    def __init__(self, name, quantity, shipping_price, selling_price):
        self.name = name
        self.quantity = quantity
        self.shipping_price = shipping_price
        self.selling_price = selling_price

    def total_shipping_cost(self):
        return self.quantity * self.shipping_price

    def selling_revenue(self, quantity_sold):
        return quantity_sold * self.selling_price

    def benefit(self, quantity_sold):
        return self.selling_revenue(quantity_sold) - self.total_shipping_cost()

    def is_profitable(self):
        return self.selling_price > self.shipping_price



def input_goods():
    name = input("Enter the good name: ")
    quantity = int(input("Enter quantity of goods: "))
    shipping_price = int(input("Enter the shipping unit price: "))
    selling_price = int(input("Enter the selling unit price: "))
    
    return Goods(name, quantity, shipping_price, selling_price)


def process_goods(good: Goods):
    print(f"\nYou buy {good.name} at {good.shipping_price} and sell at {good.selling_price}.")
    print(f"Quantity purchased: {good.quantity}")

    quantity_sold = int(input("Enter the quantity sold: "))
    benefit = good.benefit(quantity_sold)

   
    if benefit > 0:
        print(f"Profit! Total benefit: {benefit}")
    elif benefit == 0:
        print("No profit, no loss.")
    else:
        print(f"Loss! Total loss: {benefit}")

    print(f"Rentable? {good.is_profitable()}")



def main():
    goods_list = []  

    while True:
        print("\n--- Enter new goods information ---")
        good = input_goods()
        goods_list.append(good)

        process_goods(good)

        choice = input("\nDo you want to enter another goods? (yes/no): ").lower()
        if choice != "yes":
            break

    print("\n--- SUMMARY OF ALL GOODS ---")
    for g in goods_list:
        print(f"- {g.name}: Buy {g.shipping_price}, Sell {g.selling_price}, Profitable = {g.is_profitable()}")

    print("\nEnd of program. Thanks!")
    time.sleep(1)


main()
