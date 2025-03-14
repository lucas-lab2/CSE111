import math
def main():
     for i in range(13):
        radius = float(input("Please enter the radius of the can: "))
        height = float(input("Please enter the height of the can: "))
        volume = can_volume(radius, height)
        ex_surface_area = can_surface_area(radius, height)
        efficiency = storage_efficiency(volume, ex_surface_area)
        print(f"Volume: {volume: .2f}")
        print(f"Exterior Surface Area: {ex_surface_area: .2f}")
        print(f"Storage Efficiency: {efficiency:.2f}")
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