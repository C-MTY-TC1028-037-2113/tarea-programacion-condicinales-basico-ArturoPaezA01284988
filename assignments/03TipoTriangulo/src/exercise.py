def main():
    lado1 = int(input("Ingresa la medida del lado 1: "))
    lado2 = int(input("Ingresa la medida del lado 2: "))
    lado3 = int(input("Ingresa la medida del lado 3: "))
    #Escribe aquí tu código...

    if lado1<(lado2+lado3) and lado2<(lado1+lado3) and lado3<(lado1+lado2):
        if lado1==lado2==lado3:
            print('Es un Triangulo Equilatero')
        elif lado1==lado2 or lado2==lado3 or lado1==lado3:
            print('Es un Triangulo Isosceles')
        else:
            print('Es un Triangulo Escaleno')
    else:
        print('No es Triangulo')


if __name__=='__main__':
    main()
