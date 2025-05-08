def celsius_to_fahrenheit(celsius):
    
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    
    # First convert to Celsius then to Kelvin
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)

def kelvin_to_fahrenheit(kelvin):
    
    # First convert to Celsius then to Fahrenheit
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def print_menu():
    
    print("\nTemperature Converter")
    print("=" * 20)
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
    print("=" * 20)

# Main program execution starts here directly
while True:
    print_menu()
    
    try:
        choice = int(input("Enter your choice (1-7): "))
        
        if choice == 7:
            print("Thank you for using Temperature Converter :)")
            break
        
        if choice < 1 or choice > 7:
            print("Invalid choice. Please enter a number between 1 and 7.")
            continue
        
        # Get temperature input from user
        temperature = float(input("Enter the temperature value: "))
        
        # Perform conversion based on user choice
        if choice == 1:
            result = celsius_to_fahrenheit(temperature)
            print(f"{temperature}°C = {result:.2f}°F")
        
        elif choice == 2:
            result = fahrenheit_to_celsius(temperature)
            print(f"{temperature}°F = {result:.2f}°C")
        
        elif choice == 3:
            result = celsius_to_kelvin(temperature)
            print(f"{temperature}°C = {result:.2f}K")
        
        elif choice == 4:
            result = kelvin_to_celsius(temperature)
            print(f"{temperature}K = {result:.2f}°C")
        
        elif choice == 5:
            result = fahrenheit_to_kelvin(temperature)
            print(f"{temperature}°F = {result:.2f}K")
        
        elif choice == 6:
            result = kelvin_to_fahrenheit(temperature)
            print(f"{temperature}K = {result:.2f}°F")
        
    except ValueError:
        print("Invalid input. Please enter a numeric value.")