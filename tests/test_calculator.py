# tests/test_calculator.py
from app.calculator import *
import pytest

calc = Calculator()
def test_add():
    assert calc.add(4,3) == 7
    assert calc.add(0,0) == 0
    assert calc.add(1,0) == 1
    assert calc.add(0.0,3) == 3.0
    
def test_subtract():
    assert calc.subtract(4,8) == -4
    assert calc.subtract(2,1) == 1
    assert calc.subtract(4,0) == 4
    
def test_multiply():
    assert calc.multiply(4,2) == 8 
    assert calc.multiply(2,1) == 2
    assert calc.multiply(4,0) == 0
    
def test_divide():
    with pytest.raises(ZeroDivisionError):
        assert calc.divide(4,0) 
    assert calc.divide(2,1) == 2
    assert calc.divide(4,2) == 2
    
def test_power():
    assert calc.power(2,2) == 4
    assert calc.power(2,0) == 1
def test_modulo():
    assert calc.modulo(2,4) == 2
    with pytest.raises(ZeroDivisionError):
        assert calc.modulo(4,0)
    with pytest.raises(ValueError):
        assert calc.modulo("4",7)
def test_sqrt():
    with pytest.raises(ValueError):
        assert calc.sqrt(-1)
        assert calc.sqrt("e")
    assert calc.sqrt(4) == 2
    
    
    
def test_calculator_expression_positif_simple_valide():
    assert calc.calculate("1 4+8") == 22 
    assert calc.calculate("1+1") == 2 
    assert calc.calculate("7*6") == 42 
    assert calc.calculate("7*3") == 21 
    assert calc.calculate("24/8") == 3 
    assert calc.calculate("24-8") == 16 
    assert calc.calculate("54-12") == 42 
    assert calc.calculate("-4+12") == 8 
    
def test_calculator_expression_positif_complexe_valide():
    assert calc.calculate("4*3+2") == 14 
    assert calc.calculate("2+3*4*5") == 62
    assert calc.calculate("4+3*2") == 10
    assert calc.calculate("2+3*4") == 14

    
def test_calculator_expression_negatif_valide():
    assert calc.calculate("-14+8") == -6 
    assert calc.calculate("-4*3+2") == -10
    assert calc.calculate("-4+3*2") == 2
def test_calculator_expression_double_opperator():
    with pytest.raises(ValueError):
        assert calc.calculate("14++8") == "Expression invalide" 
        assert calc.calculate("14++8") == "Expression invalide" 
        
def test_calculator_expression_space():
    assert calc.calculate(" 4 * 3 + 2 ") == 14 
    with pytest.raises(ValueError,match="Erreur de logique !"):
        assert calc.calculate("14+ ") 
        assert calc.calculate(" 1 4 + ")
    

    
    