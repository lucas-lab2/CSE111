import csv

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
        next(reader)  # skip header
        for row in reader:
            if len(row) == 0:
                continue  # skip empty lines
            key = row[key_column_index]
            dictionary[key] = [row[0], row[1], float(row[2])]
    return dictionary


def main():
    try:
        # Read product data
        products_dict = read_dictionary("Week 5/products.csv", 0)

        # Print dictionary (optional - for debugging)
        # print(products_dict)

        # Open request file
        with open("Week 5/request.csv", mode="r", newline="") as request_file:
            reader = csv.reader(request_file)
            next(reader)  # skip header

            print("\nRECEIPT:")
            total_items = 0
            total_price = 0

            for row in reader:
                if len(row) == 0:
                    continue  # skip empty lines
                product_number = row[0]
                quantity = int(row[1])

                if product_number in products_dict:
                    product = products_dict[product_number]
                    name = product[1]
                    price = product[2]
                    subtotal = quantity * price

                    print(f"{name}: {quantity} @ ${price:.2f}")
                    total_items += quantity
                    total_price += subtotal
                else:
                    print(f"Unknown product number: {product_number}")

            print(f"\nTotal items: {total_items}")
            print(f"Total: ${total_price:.2f}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Protect the call to main
if __name__ == "__main__":
    main()
