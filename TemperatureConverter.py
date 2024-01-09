#===================================
#Temperature Converter by Utonion Group
#===================================

alphabet_a = "a", "A"
alphabet_b = "b", "B"
alphabet_c = "c", "C"
alphabet_d = "d", "D"
alphabet_e = "e", "E"
alphabet_f = "f", "F"

print("Do you want to convert:\n A: Celcius -> Fahrenheit\n B: Fahrenheit -> Celcius\n C: Celsius -> Kelvin\n D: Kelvin -> Celcius\n E: Fahrenheit -> Kelvin\n F: Kelvin -> Fahrenheit")
choice = input(">>")
if choice in alphabet_a: # Celcius -> Fahrenheit(A)
    celcius_fahrenheit = float(input("Celcius: "))
    answer1 = celcius_fahrenheit * 9/5 + 32
    print(f"Fahrenheit: {answer1}")
elif choice in alphabet_b:  # Fahrenheit -> Celcius(B)        
    fahrenheit_celcius = input("Fahrenheit: ")
    temperature_fahrenheit = float(fahrenheit_celcius)
    temperature_celsius = (temperature_fahrenheit - 32) * 5/9
    print(f"Celcius: {temperature_celsius}")
elif choice in alphabet_c: # Celcius -> Kelvin(C)
    celcius_kelvin = input("Celcius: ")
    temperature_celcius = float(celcius_kelvin)
    temperature_kelvin = (temperature_celcius + 273.15)
    print(f"Kelvin: {temperature_kelvin}")
elif choice in alphabet_d: # Kelvin -> Celcius(D)
    kelvin_celcius = input("Kelvin: ")
    temperature_kelvin = float(kelvin_celcius)
    temperature_celcius = (temperature_kelvin - 273.15)
    print(f"Celcius: {temperature_celcius}")
elif choice in alphabet_e: # Fahrenheit -> Kelvin(E)
    fahrenheit_kelvin = input("Fahrenheit: ")
    temperature_fahrenheit = float(fahrenheit_kelvin)
    temperature_kelvin = (temperature_fahrenheit - 32) * 5/9 + 273.15
    print(temperature_kelvin)
elif choice in alphabet_f: # Kelvin -> Fahrenheit(F)
    kelvin_fahrenheit = input("Kelvin: ")
    temprature_kelvin = float(kelvin_fahrenheit)
    temperature_fahrenheit = (temprature_kelvin - 273.15) * 1.8 + 32
    print(f"Fahrenheit: {temperature_fahrenheit}")
else:
    print("Invalid input!")
