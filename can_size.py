import math

def main():
    # List to store the results
    cans = []
    
    for i in range(12):
        name = input("Please enter the name of the can: ")
        radius = float(input("Please enter the radius of the can: "))
        height = float(input("Please enter the height of the can: "))
        
        volume = can_volume(radius, height)
        ex_surface_area = can_surface_area(radius, height)
        efficiency = storage_efficiency(volume, ex_surface_area)
        
        # Append the can name and efficiency to the list
        cans.append((name, efficiency))
    
    # Print the results
    print("\nCan Storage Efficiencies:")
    for name, efficiency in cans:
        print(f"{name} {efficiency:.2f}")

def can_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def can_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius**2
    return surface_area

def storage_efficiency(volume, surface_area):
    efficiency = volume / surface_area
    return efficiency

main()