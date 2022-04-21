""" Programa No. 3:
--programa de conversion de la temperatura grados Celsius, Farenheit y Kelvin"""

print("---------------")
print("---grados Celsius a Fareheint y Kelvin")
print("----")

#input
C=int(input("digite el valor de c ")) 

#processing
k=C+273.15
f=C+1.8+32

#output
print(str(C)+ " grados celcius son  " + str(k)+ " grados kelvin y " + str(f) + " grados frahient ")
