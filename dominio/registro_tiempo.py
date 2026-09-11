class registro_tiempo:
    def __init__(self, fecha, horas_trabajadas, tareas_realizadas):
        self.fecha = fecha
        self.__horas_trabajadas = horas_trabajadas
        self.tareas_realizadas = tareas_realizadas

    def registro_horas_trabajadas(self, horas):
        self.__horas_trabajadas = horas