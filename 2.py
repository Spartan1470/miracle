año=0
edad=0
mayor22=0

for i in range(5):
    año=int(input("ingrese año de nacimiento del estudiante: "))
    edad=2022-año
    print(f'su edad es {edad}' )
    if(edad>22):
        mayor22=mayor22+1
print(f'Los estudiantes mayores de 22 son : {mayor22}')