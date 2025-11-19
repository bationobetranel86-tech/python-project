

goods_name1 = (input("Enter the good_name: "))

goods_quantity1 =int (input("Please enter the quantity of goods: "))

shipping_unit_price1 = int(input("Enter the unit price: "))

selling_unit_price1 = int(input("Your unit selling price please:"))

print(f"You buy {goods_name1}, one for {shipping_unit_price1} and sell {selling_unit_price1}.\n Your quantity is {goods_quantity1}  ")

total_shipping_price1 = goods_quantity1*shipping_unit_price1

goods_quantity_sel1 = int(input("Enter the total quantity sell: "))



total_selling_price1 = goods_quantity_sel1*selling_unit_price1

benefit=total_selling_price1-total_shipping_price1

print(f"You make benefit. Your total selling price is {total_selling_price1} so your benefit is {benefit}")
rentable1 = selling_unit_price1 > shipping_unit_price1
print(f"Benefit ? {rentable1}")


goods_name2 = (input("Enter the good_name: "))

goods_quantity2 =int (input("Please enter the quantity of goods: "))

shipping_unit_price2 = int(input("Enter the unit price: "))

selling_unit_price2 = int(input("Your unit selling price please:"))

print(f"You buy {goods_name2}, one for {shipping_unit_price2} and sell {selling_unit_price2}.\n Your quantity is {goods_quantity2}  ")

total_shipping_price2 = goods_quantity2*shipping_unit_price2

goods_quantity_sel2 = int(input("Enter the total quantity sell: "))

total_selling_price2 = goods_quantity_sel2*selling_unit_price2

benefit2=total_selling_price2-total_shipping_price2

print(f"You make benefit. Your total selling price is {total_selling_price2} so your benefit is {benefit2}")
rentable2 = selling_unit_price2 > shipping_unit_price2
print(f"Benefit ? {rentable2}")
