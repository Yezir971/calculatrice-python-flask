# tests/test_calculator.py
from app.calculator import *
import pytest

def test_add():
    calc = Calculator()
    assert calc.add(4,3) == 7
    assert calc.add(0,0) == 0
    assert calc.add(1,0) == 1
    assert calc.add(0.0,3) == 3.0
    
def test_subtract():
    calc = Calculator()
    assert calc.subtract(4,8) == -4
    assert calc.subtract(2,1) == 1
    assert calc.subtract(4,0) == 4
    
def test_multiply():
    calc = Calculator()
    assert calc.multiply(4,2) == 8 
    assert calc.multiply(2,1) == 2
    assert calc.multiply(4,0) == 0
    
def test_divide():
    calc = Calculator()
    with pytest.raises(ZeroDivisionError):
        assert calc.divide(4,0) 
    assert calc.divide(2,1) == 2
    assert calc.divide(4,2) == 2