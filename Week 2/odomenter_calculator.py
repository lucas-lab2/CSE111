def main():
    start = float(input("Enter the starting odometer reading: "))
    end = float(input("Enter the ending odometer reading: "))
    gallons = float(input("Enter the number of gallons of gas used: "))
    mpg2 = miles_per_gallon(start, end, gallons)
    print(f"The miles per gallon is {mpg2:.2f}")


def miles_per_gallon(start_miles, end_miles, gallons):
    mpg = (end_miles - start_miles) / gallons
    
    return mpg

main()