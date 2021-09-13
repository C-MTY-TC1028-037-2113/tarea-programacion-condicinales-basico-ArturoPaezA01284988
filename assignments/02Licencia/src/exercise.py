
def main():
    edad = int(input("Ingresa tu edad: "))
    #Aquí empieza tu programa...
    if edad >= 18:
        licencia = str(input("¿Tienes Identificación oficial? (s/n): "))
        if licencia == "s":
            print("Trámite de licencia concedido")
        elif licencia == "n":
            print("No cumples requisitos")
        else:
            print("Repuesta incorrecta")
    elif edad > 0:
        print("No cumples requisitos")
    else:
        print("Respuesta incorrecta")
    
if __name__ == '__main__':
    main()
