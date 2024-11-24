EARTH_ACCELERATION_OF_GRAVITY = 9.8066500 
WATER_DENSITY = 998.2
WATER_DYNAMIC_VISCOSITY = 0.0010016

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calcula la pérdida de presión debido a los accesorios en la tubería.
    """
    P = -0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings / 2000
    return P

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calcula el número de Reynolds para un flujo laminar o turbulento en una tubería.
    """
    R = (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY
    return R

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calcula la pérdida de presión debido a la reducción de diámetro de la tubería.
    """
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter)**4 - 1)
    P = -k * WATER_DENSITY * fluid_velocity**2 / 2000
    return P

def pressure_loss_from_pipe(diameter, length, friction_factor, velocity):
    """
    Calcula la pérdida de presión debido a la fricción en la tubería.
    """
    P = friction_factor * (length / diameter) * WATER_DENSITY * velocity**2 / 2000
    return P

def water_column_height(tower_height, tank_height):
    """
    Calcula la altura de la columna de agua.
    """
    return tower_height - tank_height

def pressure_gain_from_water_height(water_height):
    """
    Calcula la ganancia de presión debido a la altura de la columna de agua.
    """
    P = WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * water_height / 1000
    return P

PVC_SCHED80_INNER_DIAMETER = 0.28687
PVC_SCHED80_FRICTION_FACTOR = 0.013
SUPPLY_VELOCITY = 1.65
HDPE_SDR11_INNER_DIAMETER = 0.048692
HDPE_SDR11_FRICTION_FACTOR = 0.018
HOUSEHOLD_VELOCITY = 1.75

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
    
    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()
