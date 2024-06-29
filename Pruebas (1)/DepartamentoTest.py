import pytest
from Mio.Departamento import Departamento
from Mio.Municipio import Municipio  # Asegúrate de que la clase Municipio esté correctamente importada

@pytest.fixture
def departamento():
    return Departamento("TestDepartamento")

@pytest.fixture
def municipio1():
    m = Municipio()
    m.asignarNombre("Municipio1")
    m.asignarPoblacion(1000)
    m.asignarTotalHombres(500)
    m.asignarEdadPromedio(30)
    m.asignarIngresoPromedio(20000)
    m.asignarTemperaturaMedia(25)
    return m

@pytest.fixture
def municipio2():
    m = Municipio()
    m.asignarNombre("Municipio2")
    m.asignarPoblacion(2000)
    m.asignarTotalHombres(1000)
    m.asignarEdadPromedio(35)
    m.asignarIngresoPromedio(25000)
    m.asignarTemperaturaMedia(30)
    return m

def test_inicializacion(departamento):
    assert departamento.darNombre() == "TestDepartamento", "El nombre inicial del departamento es incorrecto"
    assert departamento.darMunicipios() == [], "El departamento debe inicializarse sin municipios"

def test_agregar_municipio(departamento, municipio1):
    departamento.agregarMunicipio(municipio1)
    assert len(departamento.darMunicipios()) == 1, "El número de municipios después de agregar debe ser 1"
    assert departamento.darMunicipios()[0].darNombre() == "Municipio1", "El nombre del municipio agregado es incorrecto"

def test_dar_ingreso_promedio(departamento, municipio1, municipio2):
    departamento.agregarMunicipio(municipio1)
    departamento.agregarMunicipio(municipio2)
    assert departamento.darIngresoPromedio() == 22500, "El ingreso promedio del departamento es incorrecto"

def test_dar_poblacion(departamento, municipio1, municipio2):
    departamento.agregarMunicipio(municipio1)
    departamento.agregarMunicipio(municipio2)
    assert departamento.darPoblacion() == 3000, "La población total del departamento es incorrecta"

def test_dar_temperatura_media(departamento, municipio1, municipio2):
    departamento.agregarMunicipio(municipio1)
    departamento.agregarMunicipio(municipio2)
    assert departamento.darTemperaturaMedia() == 27, "La temperatura media del departamento es incorrecta"

def test_dar_total_hombres(departamento, municipio1, municipio2):
    departamento.agregarMunicipio(municipio1)
    departamento.agregarMunicipio(municipio2)
    assert departamento.darTotalHombres() == 1500, "El total de hombres del departamento es incorrecto"

def test_dar_total_mujeres(departamento, municipio1, municipio2):
    departamento.agregarMunicipio(municipio1)
    departamento.agregarMunicipio(municipio2)
    assert departamento.darTotalMujeres() == 1500, "El total de mujeres del departamento es incorrecto"

def test_dar_edad_promedio(departamento, municipio1, municipio2):
    departamento.agregarMunicipio(municipio1)
    departamento.agregarMunicipio(municipio2)
    assert departamento.darEdadPromedio() == 32, "La edad promedio del departamento es incorrecta"
