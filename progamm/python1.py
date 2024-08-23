nombre=input("Ingrese su nombre: ")
edad= int(input("Ingrese su edad: "))
altura=int(input("Ingrese su estatura: "))

if edad<12:
    print("Es un niño")
else:
    if edad>12 and edad<18:
        print("Es adolescente")
    else:
        if edad>=18:
            print("Es mayor de edad")

