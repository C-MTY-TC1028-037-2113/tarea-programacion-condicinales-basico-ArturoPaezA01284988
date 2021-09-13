def main():
    #escribe tu código abajo de esta línea
    peso = float(input('Peso en kg: '))
    altura = float(input('Altura en m:'))
    if (peso <= 0) or (altura <= 0):
        print("Revisa tus datos, alguno de ellos es erróneo.")
    else:

        i = peso/(altura**2)

        if (i>=0 and i < 20):
            print('PESO BAJO')

        elif(i>=0 and i < 25):
            print('NORMAL')

        elif(i>=0 and i < 30):
            print('SOBREPESO')

        elif(i>=0 and i < 35):
            print('OBESIDAD')

        elif(i >= 40):
            print('OBESIDAD MORBIDA')
        else:
            print("Revisa tus datos, alguno de ellos es erróneo")
        
if __name__=='__main__':
    main()