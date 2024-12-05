def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    print("1. Enter temperature in Celsius")
    print("2. Enter temperature in Fahrenheit")
    print("3. Enter temperature in Kelvin")
    choice = input("Choose an option (1/2/3): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"Fahrenheit: {celsius_to_fahrenheit(celsius):.2f}")
        print(f"Kelvin: {celsius_to_kelvin(celsius):.2f}")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"Celsius: {fahrenheit_to_celsius(fahrenheit):.2f}")
        print(f"Kelvin: {fahrenheit_to_kelvin(fahrenheit):.2f}")
    elif choice == '3':
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"Celsius: {kelvin_to_celsius(kelvin):.2f}")
        print(f"Fahrenheit: {kelvin_to_fahrenheit(kelvin):.2f}")
    else:
        print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
