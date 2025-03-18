def cels_from_fahr(farh):
    cels = (farh - 32) * 5/9
    return cels
cels = cels_from_fahr(float(input("Enter the temperature in Fahrenheit: ")))
print(f"The temperature in Celsius is {cels:.2f}.")
