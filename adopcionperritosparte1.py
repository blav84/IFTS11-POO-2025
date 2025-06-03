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