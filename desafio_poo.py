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

class SuscripcionPremium(Suscripcion):
    def __init__(self, usuario, precio_base, codigo_tarjeta, calidad_video):
        super().__init__(usuario, precio_base, codigo_tarjeta)
        self.calidad_video = calidad_video

    def reproducir_contenido(self):
        print(f"El usuario {self.usuario} está viendo contenido en máxima definición {self.calidad_video}.")


# --- Pruebas del sistema ---
if __name__ == "__main__":
    print("--- Prueba Suscripción Normal ---")
    sub_basica = Suscripcion("Carlos", 9.99, "1234567890123456")
    print(f"Tarjeta registrada: {sub_basica.obtener_tarjeta_oculta()}")
    sub_basica.reproducir_contenido()

    print("\n--- Prueba Suscripción Premium ---")
    sub_premium = SuscripcionPremium("Ana", 15.99, "9876543210987654", "4K")
    print(f"Tarjeta registrada: {sub_premium.obtener_tarjeta_oculta()}")
    sub_premium.reproducir_contenido()