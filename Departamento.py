class Departamento:

    def __init__(self, nombre):
        """
        Crea un nuevo departamento sin municipios.
        :param nombre: Nombre del departamento.
        """
        self.nombre = nombre
        self.municipios = []
        

    def agregarMunicipio(self, municipio):
        """
        Agrega un municipio nuevo al departamento.
        :param municipio: Municipio a agregar.
        """
        self.municipios.append(municipio)
        

    def darNombre(self):
        """
        Devuelve el nombre del departamento.
        :return: Nombre del departamento.
        """
        return self.nombre


    def darMunicipios(self):
        """
        Devuelve los municipios del departamento.
        :return: Municipios del departamento.
        """
        return self.municipios
    

    def darIngresoPromedio(self):
        """
        Devuelve el ingreso promedio del departamento. Este ingreso corresponde al promedio de los ingresos de los municipios que conforman el departamento.
        :return: Ingreso promedio calculado del departamento.
        """
        total_ingreso = sum(municipio.ingreso for municipio in self.municipios)
        return total_ingreso / len(self.municipios) if self.municipios else 0
    

    def darPoblacion(self):
        """
        Devuelve la población del departamento.
        :return: Población del departamento.
        """
        return sum(municipio.poblacion for municipio in self.municipios)
    

    def darTemperaturaMedia(self):
        """
        Devuelve la temperatura media del departamento. Esta temperatura corresponde al promedio de temperaturas medias de los municipios que conforman el departamento.
        :return: Temperatura media calculada del departamento.
        """
        total_temperatura = sum(municipio.temperaturaMedia() for municipio in self.municipios)
        return total_temperatura / len(self.municipios) if self.municipios else 0
    

    def darTotalHombres(self):
        """
        Devuelve el total de hombres del departamento.
        :return: Total de hombres del departamento.
        """
        return sum(municipio.totalHombres for municipio in self.municipios)
    

    def darTotalMujeres(self):
        """
        Devuelve el total de mujeres del departamento.
        :return: Total de mujeres del departamento.
        """
        return sum(municipio.totalMujeres for municipio in self.municipios)
    

    def darEdadPromedio(self):
        """
        Devuelve la edad promedio de los habitantes del departamento. Este edad corresponde al promedio de las edades (promedio) de los municipios que conforman el departamento.
        :return: Edad promedio calculada de los habitantes del departamento.
        """
        total_edad = sum(municipio.edadPromedio() for municipio in self.municipios)
        return total_edad / len(self.municipios) if self.municipios else 0
