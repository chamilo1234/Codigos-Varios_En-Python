import numpy as np

a=np.array([[-2,3,1],[2,1,-3],[4,-2,-4]])
b=np.array([5,12,7])

def ecu ():
    c=np.linalg.solve(a,b)
    j=np.allclose(np.dot(a, c), b)
    x=int(c[0])
    y=int(c[1])
    z=int(c[2])

    if j==True:
        print("La solucion es: ")
        print("\n")
        print("x= ",x)
        print("y= ",y)
        print("z= ",z)
    else:
        print("El Sistema de ecuaciones no Tiene Solución")

if np.linalg.det(a) == 0:
    x = None
    print("El Sistema de ecuaciones Tiene Infinitas ♾ Soluciones")

else:
    ecu()
input()
