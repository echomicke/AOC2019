def Calculate_fuel(mass):
    return (mass // 3) - 2

"""Returns the sum of fuel required by all modules"""
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

input_file = open("input")
fuel_input = input_file.read()
input_file.close()

fuel_input = fuel_input.splitlines()
fuel_input = list(map(int, fuel_input))
print(Total_required_fuel(fuel_input))
