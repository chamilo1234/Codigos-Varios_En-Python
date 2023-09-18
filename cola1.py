class Cola:
    #""" Representa a una cola, con operaciones de encolar y desencolar.
        #El primero en ser encolado es también el primero en ser desencolado.
    #"""
    def __init__(self):
        """ Crea una cola vacía. """
        # La cola vacía se representa por una lista vacía
        self.items=[]
    def encolar(self, x):
    #"" Agrega el elemento x como último de la cola. """
        self.items.append(x)
    def desencolar(self):
        try:
    return self.items.pop(0)
    except:
        raise ValueError("La cola está vacía")
    #""" Elimina el primer elemento de la cola y devuelve su
        valor. Si la cola está vacía, levanta ValueError. ""
    def es_vacia(self):
        return self.items == []
        
    "" Devuelve True si la cola esta vacía, False si no.""

from claseCola import Cola
q = Cola()
q.es_vacia()
True
q.encolar(1)
q.encolar(2)
q.encolar(5)
q.es_vacia()
False
q.desencolar()
1
q.desencolar()
2
q.encolar(8)
q.desencolar()
5
q.desencolar()
8
q.es_vacia()
True
q.desencolar()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "claseCola.py", line 24, in desencolar
        raise ValueError("La cola está vacía")
