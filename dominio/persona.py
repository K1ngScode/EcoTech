class persona:
    def __init__(self, nombre, direccion, telefono, correo):
        self.nombre = nombre
        self._direccion = direccion
        self._telefono = telefono
        self._correo = correo

    def actualizar_datos(self, nombre=None, direccion=None, telefono=None, correo=None):
        if nombre:
            self.nombre = nombre
        if direccion:
            self._direccion = direccion
        if telefono:
            self._telefono = telefono
        if correo:
            self._correo = correo