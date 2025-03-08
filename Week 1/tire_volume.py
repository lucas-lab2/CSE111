import math
from datetime import datetime

print("Tire Volume Calculator")
print("=======================")

while True:
    try:
        width = float(input("Enter the width of the tire in mm (ex. 205): "))
        aspect_ratio = float(input("Enter the aspect ratio of the tire (ex. 60): "))
        diameter_wheel = float(input("Enter the diameter of the wheel in inches (ex. 15): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    # Calculate the tire volume in cubic centimeters then convert to liters
    volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter_wheel)) / 10000000
    volume_liters = volume / 1000
    print(f"The approximate volume is {volume_liters:.2f} liters.")

    # Get current date in YYYY-MM-DD format
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # Append the result to volumes.txt
    with open("/Users/lucasmiranda/Documents/BYU-I/CSE111/CSE111/Week 1/volumes.txt", "a") as file:
        file.write(f"{current_date}\n")
        file.write(f"Width: {width} mm, Aspect Ratio: {aspect_ratio}, Diameter: {diameter_wheel} inches, Volume: {volume_liters:.2f} liters\n")
        file.write("-" * 50 + "\n")
    
    # Ask user if they want to perform another calculation
    while True:
        try:
            cont = int(input("Do you want to calculate the tire volume again? 1 - Yes 0 - No: "))
            if cont in (0, 1):
                break
            else:
                print("Invalid input. Please enter 1 for Yes or 0 for No.")
        except ValueError:
            print("Invalid input. Please enter 1 or 0.")
    
    if cont == 0:
        print("Exiting the program. Goodbye!")
        break
