def water_column_height(tower_height, tank_height):
    """
    Calculate the height of a column of water from a tower height and a tank wall height.
    
    Parameters:
    tower_height (float): The height of the tower.
    tank_height (float): The height of the walls of the tank.
    
    Returns:
    float: The height of the water column.
    """
    h = tower_height + (3 * tank_height) / 4
    return h

# Example usage:
tower_height = 50  # Example tower height in meters
tank_height = 10   # Example tank wall height in meters
print(water_column_height(tower_height, tank_height))
