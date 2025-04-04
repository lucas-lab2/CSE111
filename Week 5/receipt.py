"""
Extra Functionality:
- If the customer orders a Twix candy bar (product ID "C013"), the program prints a coupon for 10% off the next Twix purchase.
"""

import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters:
        filename: the name of the CSV file to read.
        key_column_index: the index of the column to use as the keys in the dictionary.
    Return: a compound dictionary that contains the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, mode="r", newline="") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header line
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = [row[0], row[1], float(row[2])]
    return dictionary

def main():
    try:
        # Read products data from products.csv
        products_dict = read_dictionary("Week 5/products.csv", 0)
        
        # Print the store name header
        store_name = "Inkom Emporium"
        print(store_name)
        
        total_items = 0
        subtotal = 0.0
        coupon_eligible = False  # Extra feature flag for coupon eligibility
        
        # Process the customer's order in request.csv
        with open("Week 5/request.csv", mode="r", newline="") as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip header line
            
            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                # Direct key lookup: will raise KeyError if product_number is not in products_dict
                product_info = products_dict[product_number]
                product_name = product_info[1]
                price = product_info[2]
                line_total = quantity * price
                
                # Print the item details
                print(f"{product_name}: {quantity} @ {price:.2f}")
                
                total_items += quantity
                subtotal += line_total
                
                # Set coupon flag if product is Twix candy bar (product ID "C013")
                if product_number == "C013":
                    coupon_eligible = True

        # Compute sales tax (6%) and total amount due
        sales_tax_rate = 0.06
        sales_tax = subtotal * sales_tax_rate
        total_due = subtotal + sales_tax
        
        # Print the summary of the receipt
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total_due:.2f}")
        
        # Thank you message
        print(f"Thank you for shopping at the {store_name}.")
        
        # Print the current date and time
        current_date_and_time = datetime.now()
        # Format similar to "Wed Nov  4 05:10:30 2020"
        formatted_datetime = current_date_and_time.strftime("%a %b %d %H:%M:%S %Y")
        print(formatted_datetime)
        
        # Extra feature: print coupon if eligible
        if coupon_eligible:
            print("COUPON: Enjoy 10% off your next Twix candy bar purchase!")
    
    except FileNotFoundError as e:
        print(f"Error: missing file\n{e}")
    except PermissionError as e:
        print(f"Error: permission denied\n{e}")
    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(e)

if __name__ == "__main__":
    main()
