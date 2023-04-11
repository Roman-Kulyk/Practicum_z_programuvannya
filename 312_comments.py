"""
This program converts a temperature inputed by user in Celsius to the Fahrenheit and Calvin"""


C = float(input('Enter your temperature: '))  #User input
F = (32 + 9/5*C)                              #Convertation to the Farenheit      
K = (C + 237.15)                              #Convertation to the Calvin

print('{0:^15.2f} Celius = {1:^15.3f} Fahrenheit = {2:^15.3f} Kelvin'.format(C, F, K)) #Output 
