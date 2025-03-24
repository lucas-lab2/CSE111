# Example 3
def main():
    # Create a list of color names.
    colors = ["red", "orange", "yellow", "green", "blue"]
    # Use a for loop to print each element in the list.
    for color in colors:
        print(color)
# Call main to start this program.
# if __name__ == "__main__":
#     main()

# The Python built-in range function creates and returns a sequence of numbers. 
# The range function accepts one, two, or three parameters as shown in example 4 and its output. 
# Many programmers use the range function in a for loop to cause the computer to repeat code once for each number in a range of numbers. 
# Example 4 shows four for loops that iterate over a range of numbers.

    # Count from zero to nine by one.
    for i in range(10):
        print(i)
    print()
    # Count from five to nine by one.
    for i in range(5, 10):
        print(i)
    print()
    # Count from zero to eight by two.
    for i in range(0, 10, 2):
        print(i)
    print()
    # Count from 100 down to 70 by three.
    for i in range(100, 69, -3):
        print(i)
# Call main to start this program.
if __name__ == "__main__":
    main()