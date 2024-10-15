def convert_temperature(value, from_unit, to_unit):
    if from_unit == "C" and to_unit == "F":
        return (value * 9/5) + 32
    elif from_unit == "F" and to_unit == "C":
        return (value - 32) * 5/9
    elif from_unit == "K" and to_unit == "C":
        return value - 273.15
    elif from_unit == "C" and to_unit == "K":
        return value + 273.15

def main():
    temp = float(input("Enter the temperature: "))
    from_unit = input("Enter the current unit (C/F/K): ").upper()
    to_unit = input("Enter the unit to convert to (C/F/K): ").upper()
    
    result = convert_temperature(temp, from_unit, to_unit)
    print(f"{temp}°{from_unit} is equal to {result}°{to_unit}")

main()
