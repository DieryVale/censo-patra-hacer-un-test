CLASS Municipio:
    def __init__(self):
        """
        Crea un nuevo municipio inicializando sus atributos en cero (0) los atributos numéricos y en cadena vacía ("") los atributos de tipo String.
        """
        self.nombre = ""
        self.ingreso_promedio = 0
        self.poblacion = 0
        self.temperatura_media = 0
        self.total_hombres = 0
        self.total_mujeres = 0
        self.edad_promedio = 0


    def darIngresoPromedio(self):
        """
        Devuelve el ingreso promedio del municipio.
        :return: Ingreso promedio del municipio.
        """
        return self.ingreso_promedio
    

    def asignarIngresoPromedio(self, pIngresoPromedio):
        """
        Establece el ingreso promedio del municipio.
        :param pIngresoPromedio: Ingreso promedio del municipio.
        """
        self.ingreso_promedio = pIngresoPromedio


    def darNombre(self):
        """
        Devuelve el nombre del municipio.
        :return: Nombre del municipio.
        """
        return self.nombre
    

    def asignarNombre(self, pNombre):
        """
        Establece el nombre del municipio.
        :param pNombre: Nombre del municipio.
        """
        self.nombre = pNombre


    def darPoblacion(self):
        """
        Devuelve la población del municipio.
        :return: Población del municipio.
        """
        return self.poblacion

    def asignarPoblacion(self, pPoblacion):
        """
        Establece la población del municipio.
        :param pPoblacion: Población del municipio.
        """
        self.poblacion = pPoblacion


    def darTemperaturaMedia(self):
        """
        Devuelve la temperatura media del municipio.
        :return: Temperatura media del municipio.
        """
        return self.temperatura_media
    

    def asignarTemperaturaMedia(self, pTemperaturaMedia):
        """
        Establece la temperatura media del municipio.
        :param pTemperaturaMedia: Temperatura media del municipio.
        """
        self.temperatura_media = pTemperaturaMedia


    def darTotalHombres(self):
        """
        Devuelve el total de hombres del municipio.
        :return: Total de hombres del municipio.
        """
        return self.total_hombres
    

    def darTotalMujeres(self):
        """
        Devuelve el total de mujeres del municipio.
        :return: Total de mujeres del municipio.
        """
        return self.total_mujeres
    

    def asignarTotalHombres(self, pTotalHombres):
        """
        Establece el total de hombres del municipio.
        :param pTotalHombres: Total de hombres del municipio.
        """
        self.total_hombres = pTotalHombres


    def darEdadPromedio(self):
        """
        Devuelve la edad promedio de los habitantes del municipio.
        :return: Edad promedio de los habitantes del municipio.
        """
        return self.edad_promedio
    

    def asignarEdadPromedio(self, pEdadPromedio):
        """
        Establece la edad promedio de los habitantes del municipio.
        :param pEdadPromedio: Edad promedio de los habitantes del municipio.
        """
        self.edad_promedio = pEdadPromedio
