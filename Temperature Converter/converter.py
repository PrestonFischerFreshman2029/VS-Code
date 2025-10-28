fahrenheit = float(input("Enter the temperature in Fahrenheit (°F): "))

celsius = (fahrenheit - 32) * 5/9
kelvin = celsius + 273.15

print(f"{fahrenheit:.1f}°F is equal to {celsius:.2f}°C and {kelvin:.2f} K")
