class FCFS:
    def processData(self, no_of_processes):
        process_data = []
        for i in range(no_of_processes):
            temporary = []
            process_id = int(input("Indique el Numero de procesos ⚙ ️:"))
            arrival_time = int(input("Ingrese Tiempo de llegada 🕤: "))
            burst_time = int(input(f"Ingrese el Tiempo de Rafaga para el Proceso ⌛ {process_id}: "))
            temporary.extend([process_id, arrival_time, burst_time])
            process_data.append(temporary)
        FCFS.schedulingProcess(self, process_data)
    def schedulingProcess(self, process_data):
        process_data.sort(key=lambda x: x[1])
        ''' funcion que ordena segun el tiempo de llegada.
        '''
        start_time = []
        exit_time = []
        s_time = 0
        for i in range(len(process_data)):
            if s_time < process_data[i][1]:
                s_time = process_data[i][1]
            start_time.append(s_time)
            s_time = s_time + process_data[i][2]
            e_time = s_time
            exit_time.append(e_time)
            process_data[i].append(e_time)
        t_time = FCFS.calculateTurnaroundTime(self, process_data)
        w_time = FCFS.calculateWaitingTime(self, process_data)
        FCFS.printData(self, process_data, t_time, w_time)
    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][3] - process_data[i][1]
            '''
            tiempo_de_respuesta = tiempo_completo - tiempo_de_llegada
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
            waiting_time = process_data[i][4] - process_data[i][2]
            '''
            tiempo_de_espera = tiempo_de_respuesta - tiempo_de_rafaga
            '''
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        '''
        tiempo_de_espera_promedio = tiempo_espera_total / no_mas_procesos
        '''
        return average_waiting_time

    def printData(self, process_data, average_turnaround_time, average_waiting_time):
    
        print("\n")
        print("Proceso  Tiempo      Tiempo        Tiempo     Tiempo       Tiempo")
        print("         lLegada     de Rafaga     Final      Respuesta    Espera")
        print("                                                    ")
        
        for i in range(len(process_data)):
            for j in range(len(process_data[i])):
                print(process_data[i][j], end="				")
            print()

        print(f'Tiempo promedio de Respuesta : {average_turnaround_time}')

        print(f'Tiempo promedio de Espera : {average_waiting_time}')

if __name__ == "__main__":

    no_of_processes = int(input("Ingrese la Cantidad de Procesos : "))

    fcfs = FCFS()
    fcfs.processData(no_of_processes)
