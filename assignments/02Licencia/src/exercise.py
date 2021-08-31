
from _typeshed import IdentityFunction


def main():
    edad = int(input("Ingresa tu edad: "))
    #Aquí empieza tu programa...
    if edad >= 18:
        Identificacion = input("¿Tienes Identificación?: ")
        if Identificacion == "si":
            print("Trámite de licencia concedido")
        elif Identificacion == "No":
            print("No cumples requisitos")
    else:
        print("No cumples requisitos")

if __name__ == '__main__':
    main()
