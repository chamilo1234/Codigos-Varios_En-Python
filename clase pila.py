
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
print("Hola bienvenido al programa de colas")
print()

p=Pila()
print(p.pilaVacia()) #1
p.InsertaDato(4)
p.InsertaDato('perro')
print(p.leerUltimo())#2
p.InsertaDato(568)
print(p.tamano())
print(p.pilaVacia())
p.InsertaDato(8.4)
print(p.Desapilar())
print(p.Desapilar())
print(p.tamano())
print(p.mostrar())
