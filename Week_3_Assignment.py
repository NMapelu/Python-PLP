def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount if it is 20% or higher."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price  # Return the original price if discount is less than 20%

# Prompt the user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(price, discount_percent)

    # Display the result
    print(f"Final price: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")
