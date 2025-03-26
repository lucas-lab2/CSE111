import random

def append_random_number(numbers):
        
    numbers.append(random.randint(1, 100))

def main():
    numbers = [16.2, 75.1, 52.3]
    print(numbers)
    append_random_number(numbers)
    print(numbers)

if __name__ == "__main__":
    main()