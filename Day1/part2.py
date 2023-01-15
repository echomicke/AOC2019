def Calculate_fuel(mass):
    return (mass // 3) - 2


def Total_required_fuel(module_mass):
    fuel_sum = 0
    for i in module_mass:
        temp_fuel_module = i
        while temp_fuel_module // 3 > 0:
            temp_fuel = Calculate_fuel(temp_fuel_module)
            if(temp_fuel < 0):
                temp_fuel = 0

            fuel_sum += temp_fuel
            temp_fuel_module = temp_fuel
    
    return fuel_sum
