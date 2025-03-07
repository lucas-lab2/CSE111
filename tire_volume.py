import math

width = float(input("Enter the width of the tire in mm (ex. 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex. 60) : "))
diamanter_wheel = float(input("Enter the diameter of the wheel in inches (ex. 15): "))
volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diamanter_wheel)) / 10000000
print(f"The approximate volume is {volume:.1f} milliliters.")
