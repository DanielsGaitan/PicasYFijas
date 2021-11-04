import Game
simple = Game.Simple()
complejo = Game.Complejo()
print('''Picas y Fijas
Hola, somos los creadores y le vamos a explicar el juego
Este juego consiste en que, a partir de un número de 4 cifras, cada una conformada con un valor del 0-9 y que no se repiten, se intente adivinar cuál es ese número con las cifras en el orden adecuado.
    Para ello, usted contará con dos tipos de pista, a saber:
        1. Pica: Es cuando usted tiene acertada una cifra pero en la posición incorrecta
        2. Fija: Es cuando usted tiene acertada una cifra en la posición correcta
    Así mismo, contará con dos modalidades de juego, a saber:
        1. Una modalidad simple donde usted le debe adivinar el número a la máquina, le dará la cifra y él le retornará las picas y las fijas
        2. Una modalidad compleja donde la máquina le adivinará a usted el número, ella le brindará la cifra y usted le retornará las picas y las fijas
Procure, en cualquiera de las dos modalidades, ingresar adecuadamente los valores solicitados, de lo contrario el programa fallará. Éxitos!!
Bueno, ya que ha entendido el juego, le deseamos buena suerte en el juego, lo dejamos con la máquina... Hasta luego

Hola... Soy la máquina, pero me puedes decir Xa3400fw4ui33, ese es mi número de serie, aunque los humanos les gusta nombres más simples, entonces dime Laura.
Selecciona una modalidad de juego, ingresa 1 para la primera modalidad expuesta y 2 para la segunda''')
m = int(input())
while m!=1 and m !=2:
    m = int(input("Reingrese un valor válido"))
if m == 1:
    simple.ejecutar()
elif m == 2:
    complejo.ejecutar()