"""Calculates and returns the amount of fuel required based on the mass"""
def Fuel_required(mass):
    fuel = mass // 3
    return fuel - 2


"""Returns the sum of fuel required based on the given fuel mass"""
def Total_fuel_required(mass):
    return sum(Fuel_required(x) for x in mass)

input_file = open("input")
fuel_input = input_file.read()
input_file.close()

fuel_input = fuel_input.splitlines()
fuel_input = list(map(int, fuel_input))
print(Total_fuel_required(fuel_input))