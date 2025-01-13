# Escribe un programa en Python que calcule el factorial de un número entero no negativo utilizando recursividad.
#  -  Crea una función llamada factorial(n) que reciba un número entero como parámetro y devuelva su factorial.
#  -  El programa debe pedir al usuario un número entero positivo y mostrar su factorial calculado mediante la función implementada.
#  -  Asegúrate de manejar correctamente el caso base para la recursión.

def factorial(num):
    numeroFactorial = []
    total = 1 
    if (num == 0):
        total = 1
    else:
        for i in range(num):
         if ((num-i)!=0):
            numeroFactorial.append(num - i)
        for prueba in numeroFactorial:
            total = total * prueba  
    return total
        


if __name__ == "__main__":
    num = int(input("Escriba usted un numero psicoloco: "))
    factorizado = factorial(num)
    print(f'El numero {num}! es igual a: {factorizado}')

