import pytest
from Mio.Censo import Censo
from Mio.Departamento import Departamento
from Mio.Municipio import Municipio

@pytest.fixture
def censo():
    return Censo()

@pytest.fixture
def departamento_vacio():
    return Departamento("Departamento Vacio")

@pytest.fixture
def departamento_lleno():
    d = Departamento("Departamento Lleno")
    m1 = Municipio()
    m1.asignarPoblacion(1000)
    m1.asignarIngresoPromedio(20000)
    m1.asignarTemperaturaMedia(25)
    m1.asignarTotalHombres(500)
    m1.asignarEdadPromedio(30)
    
    m2 = Municipio()
    m2.asignarPoblacion(2000)
    m2.asignarIngresoPromedio(25000)
    m2.asignarTemperaturaMedia(30)
    m2.asignarTotalHombres(1000)
    m2.asignarEdadPromedio(35)
    
    d.agregarMunicipio(m1)
    d.agregarMunicipio(m2)
    
    return d

def test_dar_departamento(censo):
    assert censo.darDepartamento(0).darNombre() == "Amazonas", "El nombre del primer departamento es incorrecto"
    assert censo.darDepartamento(31).darNombre() == "Vichada", "El nombre del ultimo departamento es incorrecto"

def test_dar_ingreso_promedio(censo, departamento_lleno):
    censo.departamentos[0] = departamento_lleno
    assert censo.darIngresoPromedio() == 22500, "El ingreso promedio del pais es incorrecto"

def test_dar_poblacion(censo, departamento_lleno):
    censo.departamentos[0] = departamento_lleno
    assert censo.darPoblacion() == 3000, "La poblacion total del pais es incorrecta"

def test_dar_temperatura_media(censo, departamento_lleno):
    censo.departamentos[0] = departamento_lleno
    assert censo.darTemperaturaMedia() == 27, "La temperatura media del pais es incorrecta"

def test_dar_total_hombres(censo, departamento_lleno):
    censo.departamentos[0] = departamento_lleno
    assert censo.darTotalHombres() == 1500, "El total de hombres del pais es incorrecto"

def test_dar_total_mujeres(censo, departamento_lleno):
    censo.departamentos[0] = departamento_lleno
    assert censo.darTotalMujeres() == 1500, "El total de mujeres del pais es incorrecto"

def test_dar_edad_promedio(censo, departamento_lleno):
    censo.departamentos[0] = departamento_lleno
    assert censo.darEdadPromedio() == 32, "La edad promedio del pais es incorrecta"

def test_existe_dpto_ingreso_superior(censo, departamento_lleno):
    censo.departamentos[0] = departamento_lleno
    assert censo.existeDptoIngresoSuperior(21000) == True, "Debe haber un departamento con ingreso superior a 21000"
    assert censo.existeDptoIngresoSuperior(26000) == False, "No debe haber un departamento con ingreso superior a 26000"

def test_existen_dos_dptos_igual_poblacion(censo, departamento_lleno):
    censo.departamentos[0] = departamento_lleno
    
    d2 = Departamento("Departamento Adicional")
    m3 = Municipio()
    m3.asignarPoblacion(1000)
    d2.agregarMunicipio(m3)
    
    censo.departamentos[1] = d2
    
    assert censo.existenDosDptosIgualPoblacion() == True, "Debe haber dos departamentos con igual poblacion"

def test_metodo1(censo):
    assert censo.metodo1() == "Respuesta 1", "La respuesta del metodo 1 es incorrecta"

def test_metodo2(censo):
    assert censo.metodo2() == "Respuesta 2", "La respuesta del metodo 2 es incorrecta"
