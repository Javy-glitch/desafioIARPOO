class Suscripcion:
    def __init__(self, usuario, precio_base, codigo_tarjeta):
        self.usuario = usuario
        self.precio_base = precio_base
        self.__codigo_tarjeta = str(codigo_tarjeta)

    #Método seguro (Getter)
    def obtener_tarjeta_oculta(self):
        ultimos_cuatro = self.__codigo_tarjeta[-4:]
        return f"XXXX-{ultimos_cuatro}"
    
    #Método normal
    def reproducir_contenido(self):
        print(f"El usuario {self.usuario} está viendo contenido estándar.")
