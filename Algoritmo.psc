Funcion  reiniciar_cifra ( cifra_insertar Por Referencia)
	Para i<-1 Hasta 4 Con Paso 1 Hacer
		cifra_insertar[i]<-10 //none //self.cifra_insertar()
	Fin Para
Fin Funcion

Funcion n <- cantidad_fijas(cifra, cifra_insertar) //Simple.cantidad_fijas()
	Definir fijas Como Entero
	Para i<-1 Hasta 4 Con Paso 1 Hacer
		Si cifra[i] == cifra_insertar[i] Entonces
			fijas <- fijas + 1
		Fin Si
	Fin Para
	n <- fijas
FinFuncion
Funcion n <- cantidad_picas(cifra, cifra_insertar) //Simple.cantidad_fijas()
	Definir picas Como Entero
	Para i<-1 Hasta 4 Con Paso 1 Hacer
		Para j<-1 Hasta 4 Con Paso 1 Hacer
			Si i<>j Entonces				
				Si cifra_insertar[i] == cifra[j] Entonces
					picas <- picas + 1
				Fin Si
			Fin Si
		Fin Para
	Fin Para
	n <- picas
FinFuncion

Funcion cond <- comparar_ambiguedad ( cifra, i ) //método de clase padre
	Para j<-1 hasta 4 con paso 1 hacer
		Si i<>j Entonces					
			Si cifra[i] == cifra[j] Entonces
				j<-5 
			SiNo
				cont <- cont + 1
			Fin Si					
		Fin Si			
	Fin para
	Si cont == 3 Entonces
		cond <- Falso
	SiNo
		cont <- 0
		cond <- Verdadero
	Fin Si
Fin Funcion

Funcion ejecutar_simple()
	Definir picas, fijas, intento, cont Como Entero
	Dimension cifra[4], cifra_insertar[4]
	definir cond Como Logico
	cont<-0	
	cond<-Verdadero
	intento<-1
	Para i<-1 Hasta 4 Con Paso 1 Hacer
		cifra[i]<- 10
		cifra_insertar[i]<-10
	Fin Para
	//configurar numero
	Para i<-1 Hasta 4 Con Paso 1 Hacer
		cifra[i]<-AZAR(10)
		Mientras comparar_ambiguedad(cifra, i) Hacer
			cifra[i]<-AZAR(10)
		Fin Mientras
	Fin Para
	

	//pedir numeros
	Escribir ""
	Escribir "Ahora te voy a pedir que ingreses los números"
	Mientras fijas <> 4 Hacer
		escribir "Intento ", intento
		Para i<-1 Hasta 4 Con Paso 1 Hacer
			Escribir "Ingresa la cifra numero ", i, " de tu numero"
			Leer cifra_insertar[i]
			Mientras cifra_insertar[i] > 9 o cifra_insertar[i] < 0 o comparar_ambiguedad(cifra_insertar, i) Hacer
				Si cifra_insertar[i] > 9 o cifra_insertar[i] < 0 Entonces
					Escribir "Reingresa la cifra numero ", i, " de tu numero, excede los rangos"
					Leer cifra_insertar[i]
				FinSi
				Si comparar_ambiguedad(cifra_insertar, i) entonces
						Escribir "Reingresa la cifra numero ", i, " de tu numero, ya la has ingresado previamente"
						Leer cifra_insertar[i]					
				Fin Si						
			FinMientras	
		Fin Para
		fijas<-cantidad_fijas(cifra, cifra_insertar)
		picas<-cantidad_picas(cifra, cifra_insertar)
		Escribir "Tienes ", picas, " picas y ", fijas, " fijas"
		reiniciar_cifra(cifra_insertar)
		intento <- intento + 1
	FinMientras
	Escribir "Enhorabuena, has adivinado el número en ", intento, " intentos"
FinFuncion

Funcion ejecutar_complejo()
	Definir picas Como Entero
	definir fijas como entero

FinFuncion

Algoritmo PiasFijas

	Escribir 'Picas y Fijas'
	Escribir 'Hola, somos los creadores y le vamos a explicar el juego'
	Escribir 'Este juego consiste en que, a partir de un número de 4 cifras que no se repiten, cada cifra con un valor del 0-9, se intente adivinar cuál es ese número con las cifras en el orden adecuado.'
	Escribir '    Para ello, usted contará con dos tipos de pista, a saber:'
	Escribir '        1. Pica: Es cuando usted tiene acertada una cifra pero en la posición incorrecta'
	Escribir '        2. Fija: Es cuando usted tiene acertada una cifra en la posición correcta'
	Escribir '    Así mismo, contará con dos modalidades de juego, a saber:'
	Escribir '        1. Una modalidad simple donde usted le debe adivinar el número a la máquina, le dará la cifra y él le retornará las picas y las fijas'
	Escribir '        2. Una modalidad compleja donde la máquina le adivinará a usted el número, ella le brindará la cifra y usted le retornará las picas y las fijas'
	Escribir 'Procure, en cualquiera de las dos modalidades, ingresar adecuadamente los valores solicitados, de lo contrario el programa fallará. Éxitos!!'
	Escribir 'Bueno, ya que ha entendido el juego, le deseamos buena suerte en el juego, lo dejamos con la máquina... Hasta luego'
	Escribir ''
	Escribir 'Hola... Soy la máquina, pero me puedes decir Xa3400fw4ui33, ese es mi número de serie, aunque los humanos les gusta nombres más simples, entonces dime Laura.'
	Escribir 'Selecciona una modalidad de juego, ingresa 1 para la primera modalidad expuesta y 2 para la segunda'

	Definir modalidad Como Entero
	Leer modalidad
	Mientras modalidad<>1 Y modalidad<>2 Hacer
		Escribir 'Reingrese un valor válido'
		Leer modalidad
	FinMientras

	Si modalidad=1 Entonces
		ejecutar_simple() // En este caso, refiere a Simple.ejecutar()
	SiNo
		ejecutar_complejo() // Refiere a Complejo.ejecutar()
	FinSi
	
FinAlgoritmo
