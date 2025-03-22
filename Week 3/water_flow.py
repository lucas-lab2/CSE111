# Constants
EARTH_ACCELERATION_OF_GRAVITY = 9.80665  # m/s²
WATER_DENSITY = 998.2  # kg/m³
WATER_DYNAMIC_VISCOSITY = 0.0010016  # Pa·s

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
    P = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000
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
    P = (-friction_factor * pipe_length * WATER_DENSITY * fluid_velocity**2) / (2000 * pipe_diameter)
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
    P = (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000
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
    R = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return R

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculate the pressure loss due to a reduction in pipe diameter.
    
    Parameters:
    larger_diameter (float): Diameter of the larger pipe in meters.
    fluid_velocity (float): Velocity of the fluid in the larger pipe (m/s).
    reynolds_number (float): Reynolds number for the larger pipe.
    smaller_diameter (float): Diameter of the smaller pipe in meters.
    
    Returns:
    float: Pressure loss in kilopascals (kPa).
    """
    # Calculate k using the given formula
    k = (0.1 + (50 / reynolds_number)) * (((larger_diameter / smaller_diameter) ** 4) - 1)
    
    # Calculate pressure loss P in kilopascals
    pressure_loss = (-k * WATER_DENSITY * (fluid_velocity ** 2)) / 2000
    
    return pressure_loss

def kpa_to_psi(pressure_kpa):
    """
    Convert pressure from kilopascals (kPa) to pounds per square inch (psi).
    
    Parameters:
    pressure_kpa (float): Pressure in kilopascals.
    
    Returns:
    float: Pressure in pounds per square inch.
    """
    psi = pressure_kpa * 0.145038
    return psi

# Constants for pipe properties
PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013   # (unitless)
SUPPLY_VELOCITY = 1.65                # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692  # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018    # (unitless)
HOUSEHOLD_VELOCITY = 1.75             # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)

    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY

    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    # Convert pressure to psi
    pressure_psi = kpa_to_psi(pressure)

    # Print results
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {pressure_psi:.1f} psi")

if __name__ == "__main__":
    main()