import numpy as np
def uc_c():
    uc=int(input("Carga: "))
    c=uc*(1*10**-6)
    return c
def c_c():
    c1=int(input("Carga 1: "))
    c=c1*1
def cm_m():
    cm=int(input("distancia:" ))
    m=cm/100
    return m
def m_m():
    m1=int(input("distancia:" ))
    m=m1*1
    return m
k = (9)*(10**9)
#programa
q1=()
print('datos de la carga 1 (q1)')
print('\n')
print('1.- uc a c')
print('2.- c')
print('3.- Salir')
opcion = int(input('Seleccione una opción: '))
if opcion == 1:
    q1=uc_c()
elif opcion == 2:
    q1=c_c()
elif opcion == 3:
    exit()
else:
        print('Ingrese solo números.(1/2)')
#print (q1)
print('\n')
print('datos de la carga 2 (q2)')
print('\n')
q2=()
print('1.- uc a c')
print('2.- c')
print('3.- Salir')
opcion = int(input('Seleccione una opción: '))
if opcion == 1:
    q2=uc_c()
elif opcion == 2:
    q2=c_c()
elif opcion == 3:
    exit()
else:
        print('Ingrese solo números.(1/2)')
#print (q2)
x1=()
print('\n')
print('datos de Posicion Q1 en (x)')
print('\n')
print('1.- cm a m')
print('2.- m')
print('3.- Salir')
opcion = int(input('Seleccione una opción: '))
if opcion == 1:
    x1=cm_m()
elif opcion == 2:
    x1=m_m()

elif opcion == 3:
    exit()
y1=()
print('\n')
print('datos de Posicion Q1 en (y)')
print('\n')
print('1.- cm a m')
print('2.- m')
print('3.- Salir')
opcion = int(input('Seleccione una opción: '))
if opcion == 1:
    y1=cm_m()
elif opcion == 2:
    y1=m_m()
elif opcion == 3:
    exit()
x2=()
print('\n')
print('datos de Posicion Q2 en (x)')
print('\n')
print('1.- cm a m')
print('2.- m')
print('3.- Salir')
opcion = int(input('Seleccione una opción: '))
if opcion == 1:
    x2=cm_m()
elif opcion == 2:
    x2=m_m()
elif opcion == 3:
    exit()
y2=()
print('\n')
print('datos de Posicion Q2 en (y)')
print('\n')
print('1.- cm a m')
print('2.- m')
print('3.- Salir')
opcion = int(input('Seleccione una opción: '))
if opcion == 1:
    y2=cm_m()
elif opcion == 2:
    y2=m_m()
elif opcion == 3:
    exit()
r=np.sqrt(((x2-x1)**2)+((y2-y1)**2))
F=(abs(k*q1*q2))/(r**2)
print('\n')
print("k= ",k)
print("q1= ",q1)
print("q2= ",q2)
print("x1= ",x1)
print("x2= ",x2)
print("y1= ",y1)
print("y2= ",y2)
print("r= ",r)
print("r2= ",r**2)
print("F= ",F)
print("F= ",np.format_float_scientific(F, precision = 1, exp_digits=3),"N")
a=input()
