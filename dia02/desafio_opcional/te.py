class Te:  
    # Atributos de clase
    precio_300gr = 3000
    precio_500gr = 5000

    @staticmethod
    def obtener_tiempo_recomendacion(sabor):
        """
        Devuelve el tiempo recomendado de consumo y una recomendación.
        
        Args:
            sabor (int): El sabor del té. 1: Té negro, 2: Té verde, 3: Agua de hierbas).

        Returns:
            tupla: Contiene el tiempo recomendado de consumo y una recomendación.
        """
        if sabor == 1:
            return 3, "Se recomienda consumir al desayuno."  
        elif sabor == 2:
            return 5, "Se recomienda consumir al medio día."
        elif sabor == 3:
            return 6, "Se recomienda consumir al atardecer."
        

    @staticmethod
    def obtener_precio(formato):   # Asuma que el usuario ingresará siempre un valor dentro de los permitidos (no es necesario hacer validaciones).

        """
        Devuelve el precio del té para un formato  de 300 gr o 500 gr.

        Args:
            formato (int): El formato del té. Debe ser 300 gramos o 500 gramos.

        Returns:
            int: El precio del té para el formato especificado.
        """
        
        if formato == 300:
            return Te.precio_300gr
        elif formato == 500:
            return Te.precio_500gr