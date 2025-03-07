import math

#To show creativity, I added the possiblity to run again the program based on the user's choice

while True:
    width = float(input("Enter the width of the tire in mm (ex. 205): "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire (ex. 60) : "))
    diamanter_wheel = float(input("Enter the diameter of the wheel in inches (ex. 15): "))
    volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diamanter_wheel)) / 10000000
    print(f"The approximate volume is {volume/1000:.2f} liters.")

    while True:
        cont = int(input("Do you want to calculate the tire volume again? 1 - Yes 0 - No: "))
        if cont == 1 or cont == 0:
            break  # leave loop
        print("Invalid input. Please enter 1 or 0.")
    
    if cont == 0:
        break    