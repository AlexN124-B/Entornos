# Escribe un programa en Python que determine si una palabra o frase es un palíndromo.
#  -  Crea una función llamada es_palindromo(cadena) que reciba una cadena de texto como parámetro y devuelva True si es un palíndromo, o False en caso contrario.
#  -  Ignora los espacios y convierte todas las letras a minúsculas para comparar correctamente.
#  -  El programa debe pedir al usuario una palabra o frase e indicar si es un palíndromo utilizando la función implementada
def es_palindromo (cadena):
    cadena = cadena.replace(" ", "").lower()
    palindromo = False
    inicio = 0
    fin = len(cadena)
    for i in range(len(cadena)):
        # print(f"{cadena[inicio]}=={cadena[fin-1]}")
        if(cadena[inicio]==cadena[fin-1]):
            palindromo = True
        else:
            palindromo = False
            return palindromo
        inicio +=1
        fin -= 1
    return palindromo

if __name__ == '__main__':
    cadena = "haoh"
    print(es_palindromo(cadena))
    # es_palindromo(cadena))