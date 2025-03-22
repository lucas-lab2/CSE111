
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

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculate the water pressure lost due to fittings such as 45° and 90° bends in a pipeline.
    
    Parameters:
    fluid_velocity (float): The velocity of the water flowing through the pipe in meters/second.
    quantity_fittings (int): The number of fittings in the pipeline.
    
    Returns:
    float: The lost pressure in kilopascals.
    """
    P = (-0.04 * 998.2 * fluid_velocity**2 * quantity_fittings) / 2000
    return P

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculate the Reynolds number for a pipe with water flowing through it.
    
    Parameters:
    hydraulic_diameter (float): The hydraulic diameter of the pipe in meters.
    fluid_velocity (float): The velocity of the water flowing through the pipe in meters/second.
    
    Returns:
    float: The Reynolds number (unitless).
    """
    R = (998.2 * hydraulic_diameter * fluid_velocity) / 0.0010016
    return R


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    # Constants
    water_density = 998.2  # Density of water in kg/m^3

    # Calculate the constant k
    diameter_ratio = larger_diameter / smaller_diameter
    k = 0.1 + (50 / reynolds_number) * (diameter_ratio**4 - 1)

    # Calculate the pressure loss P in kilopascals (kPa)
    pressure_loss = (-k * water_density * fluid_velocity**2) / 2000

    return pressure_loss