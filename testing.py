import Laboratorio3;
import pytest;
    
def test_sumarPorIndices_1():
    assert Laboratorio3.sumarPorIndices([12,53.2, -8], [2, 2, 0]) == -4
    
def test_sumarPorIndices_2():
    assert Laboratorio3.sumarPorIndices([12,53.2, -8], [2, 2, 8]) == -16

def test_sumarPorIndices_3():
    assert isinstance(Laboratorio3.sumarPorIndices([12,"53.2", -8], [2, 2, 8]), str) == isinstance("Error: No se puede sumar valores tipo String", str)
    
def test_sumarPorIndices_4():
    assert isinstance(Laboratorio3.sumarPorIndices([5], 0), str) == isinstance("Error: Error: El parámetro listaNumeros debe ser tipo Lista", str)
                                                                               
def test_sumarPorIndices_5():
    assert isinstance(Laboratorio3.sumarPorIndices(5, [0]), str) == isinstance("Error: Error: El parámetro listaIndices debe ser tipo Lista", str)
    
##########################################################################
                                                                               
def test_operacionesPorIndices_1():
    assert Laboratorio3.operacionesPorIndices([12,53.2, -8], [2, 2, 0], ["+", "+", "*"]) == 0
                                                                               
def test_operacionesPorIndices_2():
    assert Laboratorio3.operacionesPorIndices([12,53.2, -8], [2, 2, 8], ["+", "+", "+"]) == -16
                                                                               
def test_operacionesPorIndices_3():
    assert isinstance(Laboratorio3.operacionesPorIndices([12,"53.2", -8], [2, 2, 8], ["-", "/", "*"]), str) == isinstance("Error: No se puede sumar valores tipo String", str)
                                                                               
def test_operacionesPorIndices_4():
    assert isinstance(Laboratorio3.operacionesPorIndices([5], 0, ["//"]), str) == isinstance("Error: Error: El parámetro listaNumeros debe ser tipo Lista", str)
                                                                               
def test_operacionesPorIndices_5():
    assert isinstance(Laboratorio3.operacionesPorIndices(5, [0], ["-"]), str) == isinstance("Error: Error: El parámetro listaIndices debe ser tipo Lista", str)
                                                                               
def test_operacionesPorIndices_6():
    assert isinstance(Laboratorio3.operacionesPorIndices([5], [0], ["$"]), str) == isinstance("Error: Error: Operador no identificado", str)
                                                                               

##########################################################################
                                                                               
def test_convertirBase_1():
    assert Laboratorio3.convertirBase([0,0,1,0] , 2, 10) == 2

def test_convertirBase_2():
    assert Laboratorio3.convertirBase([2] , 10, 2) == 10

def test_convertirBase_3():
    assert Laboratorio3.convertirBase(["F","F","F"] , 16, 10) == 4095
    
def test_convertirBase_4():
    assert Laboratorio3.convertirBase([4,0,9,5] , 10, 16) == "FFF"
    
def test_convertirBase_5():
    assert Laboratorio3.convertirBase([7] , 10, 4) == 13
    
def test_convertirBase_6():
    assert Laboratorio3.convertirBase([1,3] , 4, 10) == 7
    
def test_convertirBase_7():
    assert Laboratorio3.convertirBase([2,5,3] , 10, 7) == 511

def test_convertirBase_8():
    assert Laboratorio3.convertirBase([5,1,1] , 7, 10) == 253 
