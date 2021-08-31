def main():
    #escribe tu código abajo de esta línea
    peso = float(input('Peso en kg: '))
    altura = float(input('Altura en m:'))
    Indice = peso/ altura**2
    print("Peso en kg: ", peso)

    if Indice <20:
        print('PESO BAJO')

    elif 20 <= Indice < 25:
        print('PESO NORMAL')
    
    elif 25 <= Indice < 30:
        print('SOBREPESO')
    
    elif 30 <= Indice < 40:
        print('OBESIDAD')
    
    elif Indice>=40:
      print('OBESIDAD MORBIDA')
    else:
        print('Revisa tus datos, alguno de ellos es erróneo. ')
        
if __name__=='__main__':
    main()