from Departamento import Departamento
class Censo:
    # Constantes
    TOTAL_DEPARTAMENTOS = 32

    def __init__(self):
        """
        Crea un nuevo censo.
        """
        # Crea los departamentos
        self.departamentos = [None] * self.TOTAL_DEPARTAMENTOS

        self.departamentos[0] = Departamento("Amazonas")
        self.departamentos[1] = Departamento("Antioquia")
        self.departamentos[2] = Departamento("Arauca")
        self.departamentos[3] = Departamento("Atlántico")
        self.departamentos[4] = Departamento("Bolivar")
        self.departamentos[5] = Departamento("Boyacá")
        self.departamentos[6] = Departamento("Caldas")
        self.departamentos[7] = Departamento("Caquetá")
        self.departamentos[8] = Departamento("Casanare")
        self.departamentos[9] = Departamento("Cauca")
        self.departamentos[10] = Departamento("Cesar")
        self.departamentos[11] = Departamento("Chocó")
        self.departamentos[12] = Departamento("Córdoba")
        self.departamentos[13] = Departamento("Cundinamarca")
        self.departamentos[14] = Departamento("Guainía")
        self.departamentos[15] = Departamento("Guajira")
        self.departamentos[16] = Departamento("Guaviare")
        self.departamentos[17] = Departamento("Huila")
        self.departamentos[18] = Departamento("Magdalena")
        self.departamentos[19] = Departamento("Meta")
        self.departamentos[20] = Departamento("Nariño")
        self.departamentos[21] = Departamento("Norte de Santander")
        self.departamentos[22] = Departamento("Putumayo")
        self.departamentos[23] = Departamento("Quindío")
        self.departamentos[24] = Departamento("Risaralda")
        self.departamentos[25] = Departamento("San Andrés y Providencia")
        self.departamentos[26] = Departamento("Santander")
        self.departamentos[27] = Departamento("Sucre")
        self.departamentos[28] = Departamento("Tolima")
        self.departamentos[29] = Departamento("Valle Del Cauca")
        self.departamentos[30] = Departamento("Vaupés")
        self.departamentos[31] = Departamento("Vichada")

    def darDepartamento(self, pPosicion):
        """
        Devuelve el departamento ubicado en la posición especificada.
        :param pPosicion: Posición del departamento. 0 <= pPosicion < TOTAL_DEPARTAMENTOS.
        :return: Departamento de la posición dada.
        """
        return self.departamentos[pPosicion]
        

    def darIngresoPromedio(self):
        """
        Devuelve el ingreso promedio del país.
        :return: Ingreso promedio calculado del país.
        """
        total_ingreso = sum(dpto.ingresoPromedio() for dpto in self.departamentos if dpto is not None)
        return total_ingreso / self.TOTAL_DEPARTAMENTOS
        

    def darPoblacion(self):
        """
        Devuelve la población del país.
        :return: Población del país.
        """
        return sum(dpto.poblacion for dpto in self.departamentos if dpto is not None)

        

    def darTemperaturaMedia(self):
        """
        Devuelve la temperatura media del país.
        :return: Temperatura media calculada del país.
        """
        total_temperatura = sum(dpto.temperaturaMedia() for dpto in self.departamentos if dpto is not None)
        return total_temperatura / self.TOTAL_DEPARTAMENTOS
        

    def darTotalHombres(self):
        """
        Devuelve el total de hombres del país.
        :return: Total de hombres del país.
        """
        return sum(dpto.totalHombres for dpto in self.departamentos if dpto is not None)
        

    def darTotalMujeres(self):
        """
        Devuelve el total de mujeres del país.
        :return: Total de mujeres del país.
        """
        return sum(dpto.totalMujeres for dpto in self.departamentos if dpto is not None)
    

    def darEdadPromedio(self):
        """
        Devuelve la edad promedio de los habitantes del país.
        :return: Edad promedio calculada de los habitantes del país.
        """
        total_edad = sum(dpto.edadPromedio() for dpto in self.departamentos if dpto is not None)
        return total_edad / self.TOTAL_DEPARTAMENTOS
    

    def existeDptoIngresoSuperior(self, pValor):
        """
        Indica si hay algún departamento cuyo ingreso promedio sea superior al valor dado.
        :param pValor: Valor a comparar.
        :return: True si existe al menos un departamento con mayor ingreso, False en caso contrario.
        """
        for dpto in self.departamentos:
            if dpto is not None and dpto.ingresoPromedio() > pValor:
                return True
        return False
        

    def existenDosDptosIgualPoblacion(self):
        """
        Indica si hay dos departamentos que tienen igual número de habitantes.
        :return: True si existen al menos dos departamentos con igual población y esa población es mayor a cero.
        """
        poblaciones = {}
        for dpto in self.departamentos:
            if dpto is not None:
                poblacion = dpto.poblacion
                if poblacion > 0:
                    if poblacion in poblaciones:
                        return True
                    poblaciones[poblacion] = True
        return False
    

    def metodo1(self):
        """
        Método para la extensión 1.
        :return: Respuesta 1.
        """
        pass
        

    def metodo2(self):
        """
        Método para la extensión 2.
        :return: Respuesta 2.
        """
        pass
        
