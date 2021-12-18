"""
This module contains math operation for testing.
Their purpose is to show how to use the pytest framework by example.
"""

#----------------------------------------------------------------------------------------
# Imports
#----------------------------------------------------------------------------------------

import pytest

#----------------------------------------------------------------------------------------
# A most basic function
#----------------------------------------------------------------------------------------
def test_one_plus_one():
    assert 1+1 == 2
    
#----------------------------------------------------------------------------------------
# A test function to show assertion introspection
#----------------------------------------------------------------------------------------
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

#----------------------------------------------------------------------------------------
# A test function that verifies an exception
#----------------------------------------------------------------------------------------

def test_devide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    
    assert 'division by zero' in str(e.value)

    # Multiplication test ideas 

    # two positive integers 
    # identity: multiplplying any number by 1
    # zero: multiplying any number by 0
    # positive by a negative
    # negative by a negative
    #  multiply floating numbers

    # def test_multiply_two_positive_int():
    #     assert 2 * 3 == 6

    # def test_multiply_two_positive_int():
    #     assert 1 * 99 == 99
    
    # def test_multiply_two_positive_int():
    #     assert 0 * 100 == 0

#----------------------------------------------------------------------------------------
# A test function that verifies an exception
#----------------------------------------------------------------------------------------


products = [
    (2, 3, 6),               # two positive
    (1, 99, 99),             # identity
    (0, 99, 0),              # zero
    (3, -4, -12),            # positive
    (-5, -5, 25),           # negative
    (2.5, 6.7, 16.75),       # floats
]

@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product