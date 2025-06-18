class Perro:
    def __init__(self, id, nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado, temperamento):
        self.id = id
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = estado  
        self.temperamento = temperamento

    def cambiar_estado(self, nuevo_estado):
        if nuevo_estado in ['disponible', 'reservado', 'adoptado']:    
            self.estado = nuevo_estado

    def mostrar_informacion(self):
        info = (
            f"ID: {self.id}\n"
            f"Nombre: {self.nombre}\n"
            f"Raza: {self.raza}\n"
            f"Edad: {self.edad} años\n"
            f"Tamaño: {self.tamaño}\n"
            f"Peso: {self.peso} kg\n"
            f"Salud: {self.estado_salud}\n"
            f"Vacunado: {'Sí' if self.vacunado else 'No'}\n"
            f"Estado: {self.estado}\n"
            f"Temperamento: {self.temperamento}\n"
        )
        print(info)

class UsuarioAdoptante:
    def __init__(self, nombre, dni, email, preferencias):
        self.nombre = nombre
        self.dni = dni
        self.email = email
        self.preferencias = preferencias
        self.historial_adopciones = []

    def registrarse(self):
        print(f"{self.nombre} ha sido registrado correctamente.")

    def modificar_datos(self, nombre=None, email=None, preferencias=None):
        if nombre:
            self.nombre = nombre
        if email:
            self.email = email
        if preferencias:
            self.preferencias = preferencias
        print("Datos actualizados.")

    def ver_historial(self):
        return self.historial_adopciones

class SistemaAdopcion:
    def __init__(self):
        self.perros = {}
        self.usuarios = {}

    def cargar_perro(self, perro):
        self.perros[perro.id] = perro

    def eliminar_perro(self, id_perro):
        if id_perro in self.perros:
            del self.perros[id_perro]

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.dni] = usuario

    def postular_a_perro(self, dni_usuario, id_perro):
        if dni_usuario in self.usuarios and id_perro in self.perros:
            perro = self.perros[id_perro]
            if perro.estado == 'disponible':
                perro.cambiar_estado('reservado')
                return True
        return False

    def confirmar_adopcion(self, dni_usuario, id_perro):
        if dni_usuario in self.usuarios and id_perro in self.perros:
            perro = self.perros[id_perro]
            if perro.estado == 'reservado':
                perro.cambiar_estado('adoptado')
                self.usuarios[dni_usuario].historial_adopciones.append(perro)
                return True
        return False

    def sugerir_perros(self, dni_usuario):
        if dni_usuario not in self.usuarios:
            return []

        preferencias = self.usuarios[dni_usuario].preferencias
        sugerencias = []

        for perro in self.perros.values():
            if perro.estado == 'disponible':
                if (preferencias.get('raza') == perro.raza or not preferencias.get('raza')) and \
                   (preferencias.get('edad') == perro.edad or not preferencias.get('edad')) and \
                   (preferencias.get('tamaño') == perro.tamaño or not preferencias.get('tamaño')):
                    sugerencias.append(perro)
        return sugerencias

    def mostrar_perros_disponibles(self):
        return [p for p in self.perros.values() if p.estado == 'disponible']

    def mostrar_perros_por_estado(self, estado):
        return [p for p in self.perros.values() if p.estado == estado]

    def mostrar_perros_por_usuario(self, dni_usuario):
        if dni_usuario in self.usuarios:
            return self.usuarios[dni_usuario].ver_historial()
        return []
    