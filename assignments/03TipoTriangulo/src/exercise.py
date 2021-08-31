def main():
    lado1 = int(input("Ingresa la medida del lado 1: "))
    lado2 = int(input("Ingresa la medida del lado 2: "))
    lado3 = int(input("Ingresa la medida del lado 3: "))
    #Escribe aquí tu código...

    if ((lado1 + lado2)>lado3) and ((lado3 + lado2)>lado3) and ((lado1 + lado3)>lado3):
        if lado1 == lado2 == lado3:
            print('Es un Triangulo Equilatero')
        elif lado1 == lado2 or lado3 == lado2 or lado1 == lado3:
            print('Es un Triangulo Isosceles')
        else:
            print('Es un Escaleno')
    else:
        print('No es Triangulo')


if __name__=='__main__':
    main()
