class Empleado:

    def __init__(self,id_unico, nombre, direccion, telefono, correo, FechaInicioContrato, salario):
        self._id_unico = id_unico
        self.nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo
        self._FechaInicioContrato = FechaInicioContrato
        self.__salario = salario
    
    def RegistrarEmpleado(self):
        pass
        