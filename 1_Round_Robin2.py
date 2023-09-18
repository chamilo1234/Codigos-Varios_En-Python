class RoundRobin:
    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("Indique el Numero de procesos ⚙ ️: "))

            arrival_time = int(input(f"Ingrese Tiempo de llegada para el Proceso 🕤 {process_id} : "))

            burst_time = int(input(f"Ingrese Tiempo de Rafaga para el Proceso ⌛ {process_id} : "))

            temporary.extend([process_id, arrival_time, burst_time, 0, burst_time])
            '''
            '0' Este es el estado del proceso. (0) significa no ejecutado y (1) significa ejecución completa
            
            '''
            process_data.append(temporary)
        time_slice = int(input("Ingrese Tiempo de Rodaja: "))
        RoundRobin.schedulingProcess(self, process_data, time_slice)
    def schedulingProcess(self, process_data, time_slice):
        start_time = []
        exit_time = []
        executed_process = []
        ready_queue = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])
        '''
        Ordenar procesos de acuerdo a la Hora de Llegada
        '''
        while 1:
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    present = 0
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if process_data[i][0] == ready_queue[k][0]:
                                present = 1
                    '''
                    El ciclo if anterior verifica que el siguiente proceso no sea parte de ready_queue
                    '''
                    if present == 0:
                        temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                        ready_queue.append(temp)
                        temp = []
                    '''
                    El bucle if anterior agrega un proceso a ready_queue solo si aún no está presente en él
                    '''
                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))
                    '''
                    El bucle if anterior se asegura de que el proceso ejecutado recientemente se agregue al final de ready_queue
                    '''
                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                if ready_queue[0][2] > time_slice:
                    '''
                    Si el proceso tiene un tiempo de ráfaga restante mayor que el intervalo de tiempo, se ejecutará durante un período de tiempo igual al intervalo de tiempo y luego cambiará
                    '''
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - time_slice
                    ready_queue.pop(0)
                elif ready_queue[0][2] <= time_slice:
                    '''
                    Si un proceso tiene un tiempo de ráfaga restante menor o igual que el intervalo de tiempo, completará su ejecución
                    '''
                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
                    ready_queue.pop(0)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                if normal_queue[0][2] > time_slice:
                    '''
                    Si el proceso tiene un tiempo de ráfaga restante mayor que el intervalo de tiempo, se ejecutará durante un período de tiempo igual al intervalo de tiempo y luego cambiará                    '''
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - time_slice
                elif normal_queue[0][2] <= time_slice:
                    '''
                    Si un proceso tiene un tiempo de ráfaga restante menor o igual que el intervalo de tiempo, completará su ejecución
                    '''
                    start_time.append(s_time)
                    s_time = s_time + normal_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
        t_time = RoundRobin.calculateTurnaroundTime(self, process_data)
        w_time = RoundRobin.calculateWaitingTime(self, process_data)
        RoundRobin.printData(self, process_data, t_time, w_time, executed_process)
    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            '''
            hora_de_vuelta = hora_de_finalización - hora_de_llegada
            '''
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        '''
        tiempo_promedio_de_respuesta = tiempo_de_respuesta_total / no_mas_procesos
        '''
        return average_turnaround_time
    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            '''
            tiempo_de_espera = tiempo_de_respuesta - tiempo_de_rafaga
            '''
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        '''
        tiempo_de_espera_promedio = tiempo_de_espera_total / no_mas_procesos
        '''
        return average_waiting_time
    def printData(self, process_data, average_turnaround_time, average_waiting_time, executed_process):
        process_data.sort(key=lambda x: x[0])
        '''
        Sort processes according to the Process ID
        '''
        print("\n")
        print("Proceso  Tiempo   Tiempo      Completado  Tiempo      Tiempo  Tiempo      Tiempo")
        print("         lLegada  de Rafaga               de Rafaga   Final   Respuesta   Espera")
        print("                  Restante                Inicial")
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="          ")
            print("\n")
        print(f'Tiempo promedio de Respuesta : {average_turnaround_time}')
        print(f'Tiempo promedio de Espera: {average_waiting_time}')
        print(f'Orden de Proceso: {executed_process}')
if __name__ == "__main__":
    no_of_processes = int(input("Ingrese la Cantidad de Procesos: "))
    rr = RoundRobin()
    rr.processData(no_of_processes)
