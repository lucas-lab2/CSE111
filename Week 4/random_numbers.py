import random

def append_random_numbers(numbers_list, quantity=1):
    """Appends quantity random numbers to numbers_list, rounded to 1 decimal place."""
    for _ in range(quantity):
        random_num = random.uniform(1, 100)
        rounded_num = round(random_num, 1)
        numbers_list.append(rounded_num)

def main():
    """Main function that demonstrates the append_random_numbers function."""
    numbers = [16.2, 75.1, 52.3]
    print("Initial numbers:", numbers)
    
    # First call - add one number (using default quantity)
    append_random_numbers(numbers)
    print("After adding 1 number:", numbers)
    
    # Second call - add three numbers
    append_random_numbers(numbers, 3)
    print("After adding 3 more numbers:", numbers)

if __name__ == "__main__":
    main()