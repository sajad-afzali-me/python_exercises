total_price = float(input("Enter the total amount\nprice:$ "))
if total_price <= 0:
    print("ERROR: Invalid price! Enter an amount greater than 0.")
    exit()
elif total_price < 100:
    final_price = total_price
elif 100 <= total_price < 300:
    discount_percent = 10 / 100
    final_price = total_price - (total_price * discount_percent)
else:
    discount_percent = 20 / 100
    final_price = total_price - (total_price * discount_percent)
print(f"Final price to pay (discount included): {final_price:.2f} $")
