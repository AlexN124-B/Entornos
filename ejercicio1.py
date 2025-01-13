def ES_PRIMO(num):
    contador = 0
    es_primo = False
    i = 1
    for i in range(num):
        if ((num % (i) )) == 0:
            contador += 1
    if (contador==2):
        es_primo = True
    return es_primo
if __name__ == '__main__':
    numero = int(input("Introduce un numero entero: "))
    validar = ES_PRIMO(numero)
    if (validar == True):
        print("El numero es primo")
    else:
        print("El numero no es primo")



