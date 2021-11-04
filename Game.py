import random 
#from abc import ABC, abstractmethod

class Juego: 
    def __init__(self):
        self.cifra = []
        self.picas = 0
        self.fijas = 0
        self.intento = 0
    
    
    
    #@abstractmethod #funcion abstracta
    def ejecutar (self):
        pass
    
    
    
    #@abstractmethod 
    def comparar_ambiguedad (self, a, cifra ):
        c = 0
        for i in range(len(cifra)):
            if a != i :
                if cifra[a] == cifra[i]:
                    break
                else:
                    c += 1
        if c == len(cifra) -1:
            return False
        else:
            c = 0
            return True
        
        
    #@abstractmethod 
    def reiniciar_cifra (self):
        self.cifra = []
        
        
    #@abstractmethod 
    def cantidad_picas (self):
        pass
    
    #@abstractmethod 
    def cantidad_fijas (self):
        pass
            
    
            
                
           
    
class Simple (Juego):
    def __init__(self):
        super().__init__()
        self.cifra_guardar = []
        
    
    
        
    def ejecutar (self):
        c = 0
        cond = True
        self.cifra_guardar = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
        print("Ahora te voy a pedir que ingreses los números")
        while self.fijas != 4:
            print(f"Intento {self.intento+1}")
            for i in range (4):
                while True:
                    try:
                        self.cifra.append(int(input(f"Ingrese la cifra número {i+1} de tu numero "))) 
                    
                    except ValueError:
                        print("Ingresaste un caracter diferente a un número entero, por favor ingreselo otra vez ")
                    else:
                        break
                while self.cifra[i]>9  or self.cifra[i]<0 or self.comparar_ambiguedad(i, self.cifra) :
                    if self.cifra[i] > 9 or self.cifra[i] < 0:
                        print(f"Reingresa la cifra número {i+1} de tu numero, excede los rangos ")
                        while True:
                            try:
                                self.cifra[i] = int(input(f"Ingrese la cifra número {i+1} de tu numero "))
                    
                            except ValueError:
                                print("Ingresaste un caracter diferente a un número entero, por favor ingreselo otra vez ")
                            else:
                                break
                    if self.comparar_ambiguedad(i, self.cifra):
                        print(f"Reingresa la cifra número {i+1} de tu numero, ya la has ingresado previamente ")
                        while True:
                            try:
                                self.cifra[i] = int(input(f"Ingrese la cifra número {i+1} de tu numero "))
                    
                            except ValueError:
                                print("Ingresaste un caracter diferente a un número entero, por favor ingreselo otra vez ")
                            else:
                                break
            
            
            
            self.fijas = self.cantidad_fijas()
            self.picas = self.cantidad_picas()
            print(f"Tienes {self.fijas} fijas y {self.picas} picas")
            self.reiniciar_cifra()
            self.intento += 1
            
        print(f"Enhorabuena!, has adivinaado el número en {self.intento} intentos")
        
        
    
            
    def cantidad_fijas(self):
        fijas = 0
        for i in range(4):
            if self.cifra[i] == self.cifra_guardar[i]:
                fijas += 1
        return fijas
        

                
    def cantidad_picas(self):
        picas = 0
        for i in range(4):
            for j in range(4):
                if i != j:
                    if self.cifra[i] == self.cifra_guardar[j]:
                        picas += 1
        return picas

#a = Simple()
#a.ejecutar()

class Complejo (Juego):
    def __init__(self):
        super().__init__()
        self.suma = 0
        
    def esta (self, a):
        if a < 10:
            if a in self.cifra:
                return True
            else:
                return False
        else:
            return True

    def mostrar_cifra (self):
        print("Para la cifra ", end = "")
        for i in range(len(self.cifra)):
            print(self.cifra[i], end = "")
        print("")


            
            
    def invertir (self, a, b):
        if b == 4:
            b = 0
        self.cifra[a], self.cifra[b] = self.cifra[b], self.cifra[a]
            
            
            
            
    def cantidad_fijas (self):
        while True:
            try:
                a = int(input("Por favor ingresa la cantidad de FIJAS, sé muy cuidadoso de no ingresar erróneamente los valores o el programa fallará\n"))
            except ValueError:
                print("Ingresaste un valor que no es alfanumérico, por favor reingrésalo")
            else:
                break
        while a > (4 - self.picas):
            print("La cantidad ingresada no se condice con las fijas, reingresa una adecuada, revisa si has colocado correctamente las picas")
            while True:
                try:
                    a = int(input("Por favor ingresa la cantidad de FIJAS, sé muy cuidadoso de no ingresar erróneamente los valores o el programa fallará\n"))
                except ValueError:
                    print("Ingresaste un valor que no es alfanumérico, por favor reingrésalo")
                else:
                    break
        print("En caso de que hayas ingresado erróneamente las picas o fijas")
        return a

        
        
        
    def cantidad_picas(self):
        while True:
            try:
                self.picas = int(input("Por favor ingresa la cantidad de PICAS, sé muy cuidadoso de no ingresar erróneamente los valores o el programa fallará\n"))
            except ValueError:
                print("Ingresaste un valor que no es alfanumérico, por favor reingrésalo")
            else:
                break
        while self.picas < 0 or self.picas > 4:
            print("La cantidad ingresada excede los valores, reingresa una adecuada")
            while True:
                try:
                    self.picas = int(input ("Por favor ingresa la cantidad de PICAS, sé muy cuidadoso de no ingresar erróneamente los valores o el programa fallará\n"))
                except ValueError:
                    print("Ingresaste un valor que no es alfanumérico, por favor reingrésalo")
                else:
                    break
                    
                    
                    
                    
    def ejecutar (self):
        dig, numero_fantasma, diferencia, fijaaux = 0, 0, 0, 0
        guardar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        #Dar con media cifra
        while self.suma < 2:
            self.reiniciar_cifra()
            self.cifra = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 4)

            self.mostrar_cifra()
            self.cantidad_picas()
            self.fijas = self.cantidad_fijas()
            self.suma = self.fijas + self.picas
            self.intento += 1

        #Dar con la cifra completa
        while self.suma < 4:
            for j in range(4):
                for i in range(10):
                    if not self.esta(guardar[i]):
                        dig = self.cifra[j]
                        self.cifra[j] = guardar[i]

                        self.mostrar_cifra()
                        self.cantidad_picas()
                        self.fijas = self.cantidad_fijas()
                        self.intento += 1

                        if self.fijas + self.picas > self.suma:
                            guardar[dig+1] = 10
                            self.suma = self.fijas + self.picas
                            break
                        if self.fijas + self.picas < self.suma:
                            guardar[i] = 10
                            self.cifra[j] = dig
                            break
                if self.suma == 4:
                    break
        #Dar con el orden correcto
        numero_fantasma = random.randint(0, 9)
        while self.esta(numero_fantasma):
            numero_fantasma = random.randint(0, 9)

        while self.fijas < 4 and fijaaux < 4:
            i = -1
            while i < 4:
                i += 1
                self.invertir(i, i+1)
                self.mostrar_cifra()
                self.cantidad_picas()
                fijaaux = self.cantidad_fijas()
                diferencia = fijaaux-self.fijas
                if diferencia == 2:
                    self.fijas = fijaaux
                    i+=1 #########################################################
                if diferencia == 1:
                    self.fijas = fijaaux
                    dig = self.cifra[i]
                    self.cifra[i] = numero_fantasma
                    self.mostrar_cifra()
                    self.cantidad_picas()
                    fijaaux = self.cantidad_fijas()

                    self.intento += 1
                    if fijaaux - self.fijas == 0:
                        self.cifra[i] = dig
                        i+=1#############################################################
                    if fijaaux - self.fijas == -1:
                        self.cifra[i] = dig

                if diferencia == -1:
                    self.invertir(i, i+1)
                    self.fijas = fijaaux
                    dig = self.cifra[i]
                    self.cifra[i] = numero_fantasma

                    self.mostrar_cifra()
                    self.cantidad_picas()
                    fijaaux = self.cantidad_fijas()
                    self.intento += 1

                    if fijaaux - self.fijas == 0:
                        self.cifra[i] = dig
                        self.mostrar_cifra()
                        self.cantidad_picas()
                        self.fijas = self.cantidad_fijas()

                    elif fijaaux - self.fijas == 1:
                        self.cifra[i] = dig
                        self.fijas = fijaaux
                        i+=1 #####################################
                if diferencia == -2:
                    self.invertir(i, i+1)
                    self.fijas = fijaaux
                    i+=1 #####################################################
                if fijaaux >= 4 or self.fijas >=4:
                    fijaaux, self.fijas = 4, 4
                    self.intento += 1
                    break
                self.intento += 1

            if fijaaux < 4 or self.fijas < 4:
                i = -1
                while i < 2:
                    i += 1
                    self.invertir(i, i + 2)
                    self.mostrar_cifra()
                    self.cantidad_picas
                    fijaaux = self.cantidad_fijas
                    self.intento += 1
                    if fijaaux - self.fijas == 2:
                        self.fijas, fijaaux = 4, 4
                        break
                    if fijaaux - self.fijas == -2:
                        self.invertir(i, i + 2)
        print(f"He adivinado el número en {self.intento} intentos")


                    

                
        
            
            
            
            
            
            
            
            
            
            
            
            
                            
                        
                
        
    
    
    
    
    
    
    
    
    
    
    
    
    





















