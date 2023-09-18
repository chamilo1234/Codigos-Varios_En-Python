# Ejercicio de Cola Cola, Primero en entrar, Primero en Salirsalir

class Cola:

    #Crea la Lista Cola

    def __init__(self):
        self.datos = []

    #Pregunta la Cantidad de Datos que hay en cola de la lista
    def cantidad(self):
        return len(self.datos)
               
    #Insertar un dato en la Cola de la lista
    def Cinsertar(self, dato):
        self.datos.insert(0, dato)
    
    #Extrae el primer dato de la Cola
    def Cextraer(self):
        if self.cantidad():
            return self.datos.pop()
        else:
            return None
    
    #Muestra el Primer Dato de la Cola
    def CdatoUno(self):
        if self.cantidad():
            return self.datos[-1]
    
    #Muestra el Ultimo dato de la Cola
    def CDatoUltimo(self):
        if self.cantidad():
            return self.datos[0]
    #para limpiar la cola y empezar nuevamente
    def limpiar (self):
        del self.datos
    #muestra el tamaño  que tiene la Cola
    def tamano(self):
         return len(self.datos)
    #muestra los elementos que contiene la cola
    def mostrar (self):
        print(self.datos)
#***********************************
#Programa Principal
print("DESARROLLADO POR JOSE ARMANDO BENAVIDES CANCHALA Y JUAN CAMILO MORALES LOPEZ.")
print()
print("Bienvenido este es un programa impementar el funcionamiento de una Cola.")
print()
print(input("Para Crear la Cola oprima Enter "))

numeros = Cola()


#**************************
#creamos una funcion  menu para llamar las funciones de cola
def menu():
    print()
    print ("Selecciona una opción.")
    print()
    print ("1: Verifica si la Cola esta  vacia.")
    print ("2: encolar un elemento.")
    print ("3: descolar un elemento.")
    print ("4: ver el frente de la Cola.")
    print ("5: ver final de la Cola")
    print ("6: cantidad de elementos en la Cola.")
    print ("7: mostrar los elementos de la Cola.")
    print ("8: eliminar Cola.")
    print ("9: salir.")
#es un ciclo que repite el llamado a las opciones segun la condicion de salida
while True:
    # Mostramos el menu
    menu()
        # solicitamos que elija una opción el usuario
    print()
    opcionMenu = input("inserta un numero valor >> ")
    if opcionMenu=="1":
        print ("")
        input("Has pulsado la opción 1...\npara verificar si la Cola esta vacia pulsa una tecla para continuar")
        print()
        if  numeros.cantidad()==True:
            print("la Cola tiene elementos.")
        else:
            print("la Cola esta vacia.")
        print()
    elif opcionMenu=="2":
        print ("")
        input("Has pulsado la opción 2...\npara insertar datos pulsa una tecla para continuar")
        dato=input("Ingrese un dato a encolar: ")
        numeros.Cinsertar(dato)
    elif opcionMenu=="3":
        print ("")
        input("Has pulsado la opción 3...\npara descolar un dato pulsa una tecla para continuar")
        print()
        print("El Dato descolado es: ",numeros.Cextraer())
        print()
        
    elif opcionMenu=="4":
        print()
        input("Has pulsado la opción 4...\npara ver el frente de la cola pulsa una tecla para continuar")
        print("El elemento al frente de la cola es: ",numeros.CdatoUno())
        
    elif opcionMenu=="5":
        print()
        input("Has pulsado la opción 5...\npara ver el final de la cola pulsa una tecla para continuar")
        print("El elemento al final de la cola es: ",numeros.CDatoUltimo())
    elif opcionMenu=="6":
        print()
        input("Has pulsado la opción 6...\npara mostrar la cantidad de elementos en la Cola pulsa una tecla para continuar")
        print("la cantidad de elementos de la cola son: ",numeros.tamano())
        
    elif opcionMenu=="7":
        print()
        input("Has pulsado la opción 7...\npara mostrar los elementos de la Cola pulsa una tecla para continuar")
        print("los elementos de la cola son: ",numeros.mostrar())
        
    elif opcionMenu=="8":
        print()
        input("Has pulsado la opción 8...\npara eliminar la cola pulsa una tecla para continuar")
        numeros.limpiar()
        
    elif opcionMenu=="9":
        exit()
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npara volver al menu inicial pulsa una tecla para continuar")
        


