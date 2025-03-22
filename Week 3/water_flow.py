
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

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculate the water pressure lost due to friction between the water and the walls of a pipe.
    
    Parameters:
    pipe_diameter (float): The diameter of the pipe in meters.
    pipe_length (float): The length of the pipe in meters.
    friction_factor (float): The pipe’s friction factor.
    fluid_velocity (float): The velocity of the water flowing through the pipe in meters/second.
    
    Returns:
    float: The lost pressure in kilopascals.
    """
    P = (-friction_factor * pipe_length * 998.2 * fluid_velocity**2) / (2000 * pipe_diameter)
    return P




