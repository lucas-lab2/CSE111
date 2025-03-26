import random

def append_random_number(numbers_list):
        
    random_float = random.uniform(1, 100)  # Generates a random float between 1 and 100
    numbers_list.append(round(random_float, 1))  # Rounds to 1 decimal place (like your origina

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_number(numbers)
    print(numbers)

if __name__ == "__main__":
    main()