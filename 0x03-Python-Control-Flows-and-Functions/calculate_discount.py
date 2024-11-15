#!/usr/bin/python3
"""Calculate_discount module"""

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_percent /= 100
        discounted_price = price * discount_percent
        final_price = price - discounted_price
        return final_price
    else:
        return price


original_price = float(input("Enter original price of an item: "))
discount_percentage = float(input("Enter the discount percentage: "))

finalPrice = calculate_discount(original_price, discount_percentage)

if finalPrice < original_price:
    print(finalPrice)
else:
    print(original_price)

