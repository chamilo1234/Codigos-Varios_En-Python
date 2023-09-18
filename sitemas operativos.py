def sjf(rafaga_ordenada, rafaga):
    print(f"proceso      rafaga de CPU    tiempo de espera    tiempo de respuesta")
    i = 0
    tiempo_espera = 0
    tiempo_repuesta = 0
    lista1 = []
    lista2 = []


    while (i < len(rafaga_ordenada)):
        tiempo_respuesta += rafaga_ordenada[i]
        print(f=' p ' + str(rafaga.index(rafaga_ordenada[i])+1) + str(rafaga_ordenada[i]) + str(tiempo_espera) + ragafa[rafaga.index(rafaga_ordenada[i])]) == -1
        lista1.append(tiempo_espera)
        lista2.append(tiempo_respuesta)
        tiempo_espera += rafaga_ordenada[i]
        i += 1
    return(lista1, lista2)

entrada1 = int(input("por favor introduzca el numero de procesos que va a ejecutar: "))
rafaga_tiempo = []

for i in range (entrada1):
    rafaga_tiempo.append(int(input("por favor introduza la rafaga de CPU: "+ str(i + 1) + ': ')))

lis = sjf(sorted(rafaga_tiempo), rafaga_tiempo)
print("promedio de tiempo de espera: "+ str(sum(lis[0]) / len(list[0])))
print("promedio e tiempo de respuesta: "+ str(sum(list[1]) / len(lis[1])))
