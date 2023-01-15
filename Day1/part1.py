"""Calculates and returns the amount of fuel required based on the mass"""
def Fuel_required(mass):
    fuel = mass // 3
    return fuel - 2


def Total_fuel_required(mass):
    total_fuel = 0
    for x in mass:
        total_fuel += Fuel_required(x)

    return total_fuel