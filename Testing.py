import Laboratorio5;
import pytest;
    
def test_eliminarRepetidos_1():
    assert Laboratorio5.eliminarRepetidos( [12, 78, 12, 0, 5.2, "abc", 0, 12, 5.2, 12] ) == [78, "abc"]
    
def test_eliminarRepetidos_2():
    assert Laboratorio5.eliminarRepetidos( [12, 5.2, 12] ) == [ 5.2]
    
def test_sumaImparesPares_1():
    assert Laboratorio5.sumaImparesPares([0,2,3,4], [4, 8, 6, 0]) == [13, 14]
    
def test_sumaImparesPares_2():
    assert Laboratorio5.sumaImparesPares([10, 0], [100, 2]) == [110, 2]
    
def test_sumaImparesPares_3():
    assert isinstance(Laboratorio5.sumaImparesPares([1,2], "dos"), str) == isinstance("Error: segundo argumento debe ser entero", str)
    
def test_convertirBase_1():
    assert Laboratorio5.convertirBase([0,0,1,0] , 2, 10) == 2

def test_convertirBase_2():
    assert Laboratorio5.convertirBase([2] , 10, 2) == 10

def test_convertirBase_3():
    assert Laboratorio5.convertirBase(["F","F","F"] , 16, 10) == 4095
    
def test_convertirBase_4():
    assert Laboratorio5.convertirBase([4,0,9,5] , 10, 16) == "FFF"
    
def test_convertirBase_5():
    assert Laboratorio5.convertirBase([7] , 10, 4) == 13
    
def test_convertirBase_6():
    assert Laboratorio5.convertirBase([1,3] , 4, 10) == 7
    
def test_convertirBase_7():
    assert Laboratorio5.convertirBase([2,5,3] , 10, 7) == 511

def test_convertirBase_8():
    assert Laboratorio5.convertirBase([5,1,1] , 7, 10) == 253 
