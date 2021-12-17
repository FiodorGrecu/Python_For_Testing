"""
This module contains math operation for testing.
Their purpose is to show how to use the pytest framework by example.
"""
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

