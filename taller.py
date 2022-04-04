
negativos=0
multiplo3=0
multiplo2=0
numero=0
n=0
i=0
n=int(input("Cuantos numeros desea ingresar? "))

for i in range (n):
    numero=int(input("Ingrese numero: "))

    if(numero % 2==0):
        multiplo2=multiplo2+1
    if(numero % 3==0):
        multiplo3=multiplo3+1
    if(numero<0):
        negativos=negativos+1
    if(numero % 2==0 and numero % 3==0):
        multiplo2=multiplo2+1
        multiplo3=multiplo3+1
print(f'cantidad de multiplos de 2: {multiplo2}')
print(f'cantidad de multiplos de 3: {multiplo3}')
print(f'cantidad de negativos {negativos}').
