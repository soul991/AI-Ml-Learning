'''Q6.
Ask the user for a temperature in Celsius (string input). Convert it to float,
then calculate and print temperature in Fahrenheit.
Conversion formula: F ahrenheit Temp= (Celsius Temp * (9/5)) + 32'''

c = input("Enter the temperature in celcius: ")
d = float(c)

f = (d*(9/5))+32

print("The temperature in farenhet is", f)