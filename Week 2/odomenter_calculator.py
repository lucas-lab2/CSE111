def main():
    start = float(input("Enter the starting odometer reading: "))
    end = float(input("Enter the ending odometer reading: "))
    gallons = float(input("Enter the number of gallons of gas used: "))
    mpg2 = miles_per_gallon(start, end, gallons)
    print(f"The miles per gallon is {mpg2:.2f}")
    print(f"{lp100k_from_mpg(mpg2):.2f} liters per 100 kilometers")


def miles_per_gallon(start_miles, end_miles, gallons):
    mpg = (end_miles - start_miles) / gallons
    
    return mpg
def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k

if __name__ == "__main__":
    main()