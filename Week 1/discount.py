import datetime


while True:
    # Get the current day of the week (Monday=0, Tuesday=1, ..., Sunday=6)
    today = datetime.datetime.now()
    weekday = today.weekday()

    # Determine if today is Tuesday (1) or Wednesday (2)
    is_discount_day = weekday in [1, 2]

    # Calculate subtotal by repeatedly asking for price and quantity
    subtotal = 0.0
    print("Enter the price and quantity for each item.")
    print("Enter 0 for the price when you are finished.\n")

    while True:
        try:
            price = float(input("Enter price: $"))
        except ValueError:
            print("Invalid input. Please enter a numeric value for price.")
            continue

        # If price is 0, exit the loop
        if price == 0:
            break

        try:
            quantity = float(input("Enter quantity: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value for quantity.")
            continue

        subtotal += price * quantity

    print(f"\nSubtotal: ${subtotal:.2f}")

    # Initialize discount and compute discounted subtotal if applicable
    discount_amount = 0.0
    if is_discount_day:
        if subtotal >= 50:
            discount_amount = 0.10 * subtotal
            subtotal -= discount_amount
        else:
            # Stretch challenge: show additional amount needed to qualify for discount
            additional_needed = 50 - subtotal
            print(f"Additional amount needed to qualify for discount: ${additional_needed:.2f}")

    # Compute sales tax of 6% on the (possibly discounted) subtotal
    sales_tax = 0.06 * subtotal
    total_due = subtotal + sales_tax

    # Print the results
    if discount_amount > 0:
        print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total Amount Due: ${total_due:.2f}")

    while True:
        cont = int(input("Do you want to calculate your discount again? 1 - Yes 0 - No: "))
        if cont == 1 or cont == 0:
            break  # leave loop
        print("Invalid input. Please enter 1 or 0.")
    
    if cont == 0:
        break
