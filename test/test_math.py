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