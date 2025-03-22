
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

def pressure_gain_from_water_height(height):
    """
    Calculate the pressure caused by Earth's gravity pulling on the water stored in an elevated tank.
    
    Parameters:
    height (float): The height of the water column in meters.
    
    Returns:
    float: The pressure in kilopascals.
    """
    P = (998.2 * 9.80665 * height) / 1000
    return P



