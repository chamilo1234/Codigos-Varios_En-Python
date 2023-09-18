class Pila:
    def __init__(self):
        self.dato = []

    def pilaVacia(self):
        return self.dato == []

    def InsertaDato(self, dato):
        self.dato.append(dato)

    def Desapilar(self):
        return self.dato.pop()

    def leerUltimo(self):
        return self.dato[len(self.dato)-1]

    def tamano(self):
         return len(self.dato)

    def limpiar (self):
        del self.dato

    def mostrar (self):
        print("los elementos de la pila son: ")
        print(self.dato)
    
    
        
#Programa Principal
print()
print("Hola bienvenido al programa de pilas")
print()

print(input('para crear una pila presione enter en el teclado!)'))
p=Pila()
m1='p'
m2='p.InsertaDato'
m3='p.Desapilar'
m4='p.leerUltimo'
m5="p.tamano"
m6="p.mostrar"
m7="p.limpiar"
print("menu de operaciones con pilas.")
print()
print("1: comprobar lista vacia.")
print("2: insertar dato.")
print("3: desapilar dato.")
print("4: mostrar ultimo dato.")
print("5: mostrar el tamaño de la pila.")
print("6: mostrar datos de la pila.")
print("7: limpiar pila.")
print("8: salir.")
print()
opc=input("seleccione una opcion: ")
if opc == "1":
     
     print("la lista esta vacia: ?",p.pilaVacia())
  #return  opc

         
    
#elif opc == "2":
    #p.InsertaDato(str(input(print("ingrese dato"))))
    

#else:
    #print("gh")



#p=Pila()
#print(p.pilaVacia()) #1
#p.InsertaDato(4)
#p.InsertaDato('perro')
#print(p.leerUltimo())#2
#p.InsertaDato(568)
#print(p.tamano())
#print(p.pilaVacia())
#p.InsertaDato(8.4)
#print(p.Desapilar())
#print(p.Desapilar())
#print(p.tamano())
#print(p.mostrar())
