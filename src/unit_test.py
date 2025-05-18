# -*- coding: utf-8 -*-
"""
Li Wen, Stephanie Yow
Class: CS 521 - Spring 1
Date: Sat Feb 14 2025
Final Project
Description: Cooking and Baking Unit Converter (unit_test.py)
Provide unit tests that prove public methods of the class Convert work 
as expected, using assert statements.
"""

from conversion import Convert

def test_convert_to_tablespoon():
    '''
    Unit test that proves public method to_tablespoon() of class Convert
    works as expected.
    '''
    convert_volume = Convert('Volume', '2', 'Cup', 'Tablespoon')
    assert round(convert_volume.to_tablespoon(), 2) == 32.00, \
        '2 cups should be 32.00 tablespoons.'

def test_convert_to_oz():
    '''
    Unit test that proves public method to_oz() of class Convert works
    as expected.
    '''
    convert_weight = Convert('Weight', '1.5', 'Pound', 'Ounce')
    assert round(convert_weight.to_oz(), 2) == 24.00, \
        '1.5 pounds should be 24.00 ounces.'    
    
def test_convert_to_f():
    '''
    Unit test that proves public method to_f() of class Convert works
    as expected.
    '''
    convert_temp = Convert('Temperature', '999.99', 'Celsius', 'Fahrenheit')
    assert round(convert_temp.to_f(), 2) == 1831.98, \
        '999.99°C should be 1,831.98°F.'

if __name__ == '__main__':
    test_convert_to_tablespoon()
    test_convert_to_oz()
    test_convert_to_f()
    print('Passed 3 unit tests.')