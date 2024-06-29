import pytest
from Mio.Municipio import Municipio  # Asegúrate de que la clase Municipio esté correctamente importada

@pytest.fixture
def municipio():
    return Municipio()

def test_inicializacion(municipio):
    assert municipio.darNombre() == "", "El nombre inicial debe ser una cadena vacía"
    assert municipio.darPoblacion() == 0, "La población inicial debe ser 0"
    assert municipio.darTotalHombres() == 0, "El total de hombres inicial debe ser 0"
    assert municipio.darEdadPromedio() == 0, "La edad promedio inicial debe ser 0"
    assert municipio.darIngresoPromedio() == 0, "El ingreso promedio inicial debe ser 0"
    assert municipio.darTemperaturaMedia() == 0, "La temperatura media inicial debe ser 0"

def test_asignar_nombre(municipio):
    municipio.asignarNombre("TestName")
    assert municipio.darNombre() == "TestName", "El nombre asignado es incorrecto"

def test_asignar_poblacion(municipio):
    municipio.asignarPoblacion(1000)
    assert municipio.darPoblacion() == 1000, "La población asignada es incorrecta"

def test_asignar_total_hombres(municipio):
    municipio.asignarTotalHombres(500)
    assert municipio.darTotalHombres() == 500, "El total de hombres asignado es incorrecto"

def test_asignar_edad_promedio(municipio):
    municipio.asignarEdadPromedio(35)
    assert municipio.darEdadPromedio() == 35, "La edad promedio asignada es incorrecta"

def test_asignar_ingreso_promedio(municipio):
    municipio.asignarIngresoPromedio(20000)
    assert municipio.darIngresoPromedio() == 20000, "El ingreso promedio asignado es incorrecto"

def test_asignar_temperatura_media(municipio):
    municipio.asignarTemperaturaMedia(25)
    assert municipio.darTemperaturaMedia() == 25, "La temperatura media asignada es incorrecta"

def test_dar_total_mujeres(municipio):
    municipio.asignarPoblacion(1000)
    municipio.asignarTotalHombres(600)
    assert municipio.darTotalMujeres() == 400, "El total de mujeres calculado es incorrecto"

