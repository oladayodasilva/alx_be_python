# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT = 32  # Constant offset used in conversions


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factor."""
    return (fahrenheit - FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT


# Main program flow
try:
    # Prompt user for temperature
    temp_input = input("Enter the temperature to convert: ").strip()
    
    # Validate numeric input
    if not temp_input.replace('.', '', 1).isdigit() and not (temp_input.startswith('-') and temp_input[1:].replace('.', '', 1).isdigit()):
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    temperature = float(temp_input)

    # Ask user for unit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    elif unit == "C":
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

except ValueError as e:
    print(e)
