# -*- coding: utf-8 -*-
"""
Li Wen, Stephanie Yow
Class: CS 521 - Spring 1
Date: Sat Feb 14 2025
Final Project
Description: Cooking and Baking Unit Converter (conversion.py)
User-defined classes Convert and Retrieve. Former converts units of 
measurement, latter gets recent conversions.
"""

from datetime import datetime
from collections import OrderedDict

class Convert:
    '''
    Class with methods that calculate, print, store and output conversions in 
    append mode to a text file.
    '''
    def __init__(self, category: str, from_value: str,
                 from_unit: str, to_unit: str):
        ''' 
        A conversion has a measurement category, to-from units of measurement, 
        a conversion value and a dictionary to store it.
        '''
        self.category = category
        self.from_value = from_value
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.__log = OrderedDict()
    
    def __str__(self):
        '''
        Magic method that informs the user of a conversion in progress.
        '''
        return 'Converting...'
    
    def to_ml(self):
        '''
        Public method that converts volume units of measurement to millilitres.
        '''
        if self.from_unit == 'Teaspoon':
            to_value = float(self.from_value) * 4.9289192708
            print(f'{self.from_value} teaspoon(s) is {to_value:,.2f}ml.')
        elif self.from_unit == 'Tablespoon':
            to_value = float(self.from_value) * 14.786757812
            print(f'{self.from_value} tablespoon(s) is', 
                  f'{to_value:,.2f}ml.')
        elif self.from_unit == 'Cup':
            to_value = float(self.from_value) * 236.588125
            print(f'{self.from_value} cup(s) is', 
                  f'{to_value:,.2f}ml.')
        else:
            to_value = float(self.from_value)
            print(f'{self.from_value}ml is {to_value:,.2f}ml.')
        return to_value
    
    def to_teaspoon(self):
        '''
        Public method that converts volume units of measurement to teaspoons.
        '''        
        if self.from_unit == 'Millilitre':
            to_value = float(self.from_value) * 0.2028842318
            print(f'{self.from_value}ml is {to_value:,.2f} teaspoon(s).')
        elif self.from_unit == 'Tablespoon':
            to_value = float(self.from_value) * 3
            print(f'{self.from_value} tablespoon(s) is', 
                  f'{to_value:,.2f} teaspoon(s).')
        elif self.from_unit == 'Cup':
            to_value = float(self.from_value) * 48
            print(f'{self.from_value} cup(s) is',
                  f'{to_value:,.2f} teaspoon(s).')
        else:
            to_value = float(self.from_value)
            print(f'{self.from_value} teaspoon(s) is', 
                  f'{to_value:,.2f} teaspoon(s).')
        return to_value  
    
    def to_tablespoon(self):
        '''
        Public method that converts volume units of measurement to tablespoons.
        '''
        if self.from_unit == 'Millilitre':
            to_value = float(self.from_value) * 0.0676280773
            print(f'{self.from_value}ml is', 
                  f'{to_value:,.2f} tablespoon(s).')
        elif self.from_unit == 'Teaspoon':
            to_value = float(self.from_value) * 0.3333333333
            print(f'{self.from_value} teaspoon(s) is', 
                  f'{to_value:,.2f} tablespoon(s).')
        elif self.from_unit == 'Cup':
            to_value = float(self.from_value) * 16
            print(f'{self.from_value} cup(s) is', 
                  f'{to_value:,.2f} tablespoon(s).')
        else:
            to_value = float(self.from_value)
            print(f'{self.from_value} tablespoon(s) is', 
                  f'{to_value:,.2f} tablespoon(s).')    
        return to_value
    
    def to_cup(self):
        '''
        Public method that converts volume units of measurement to cups.
        '''
        if self.from_unit == 'Millilitre':
            to_value = float(self.from_value) * 0.0042267548
            print(f'{self.from_value}ml is {to_value:,.2f} cup(s).')
        elif self.from_unit == 'Teaspoon':
            to_value = float(self.from_value) * 0.0208333333
            print(f'{self.from_value} teaspoon(s) is', 
                  f'{to_value:,.2f} cup(s).')
        elif self.from_unit == 'Tablespoon':
            to_value = float(self.from_value) * 0.0625
            print(f'{self.from_value} tablespoon(s) is', 
                  f'{to_value:,.2f} cup(s).')
        else:
            to_value = float(self.from_value)
            print(f'{self.from_value} cup(s) is',
                  f'{to_value:,.2f} cup(s).')       
        return to_value
    
    def to_g(self):
        '''
        Public method that converts weight units of measurement to grams.
        '''
        if self.from_unit == 'Kilogram':
            to_value = float(self.from_value) * 1000
            print(f'{self.from_value} kilogram(s) is', 
                  f'{to_value:,.2f} gram(s).')
        elif self.from_unit == 'Ounce':
            to_value = float(self.from_value) * 28.3495
            print(f'{self.from_value} ounce(s) is',
                  f'{to_value:,.2f} gram(s).')
        elif self.from_unit == 'Pound':
            to_value = float(self.from_value) * 453.5924
            print(f'{self.from_value} pound(s) is', 
                  f'{to_value:,.2f} gram(s).')
        else:
            to_value = float(self.from_value)
            print(f'{self.from_value} gram(s) is',
                  f'{to_value:,.2f} gram(s).')
        return to_value        
    
    def to_kg(self):
        '''
        Public method that converts weight units of measurement to kilograms.
        '''
        if self.from_unit == 'Gram':
            to_value = float(self.from_value) * 0.001
            print(f'{self.from_value} gram(s) is', 
                  f'{to_value:,.2f} kilogram(s).')
        elif self.from_unit == 'Ounce':
            to_value = float(self.from_value) * 0.0283495
            print(f'{self.from_value} ounce(s) is', 
                  f'{to_value:,.2f} kilogram(s).')
        elif self.from_unit == 'Pound':
            to_value = float(self.from_value) * 0.453592
            print(f'{self.from_value} pound(s) is',
                  f'{to_value:,.2f} kilogram(s).')
        else:
            to_value = float(self.from_value)
            print(f'{self.from_value} kilogram(s) is', 
                  f'{to_value:,.2f} kilogram(s).')
        return to_value

    def to_oz(self):
        '''
        Public method that converts weight units of measurement to ounces.
        '''
        if self.from_unit == 'Gram':
            to_value = float(self.from_value) * 0.0352739907
            print(f'{self.from_value} gram(s) is',
                  f'{to_value:,.2f} ounce(s).')
        elif self.from_unit == 'Kilogram':
            to_value = float(self.from_value) * 35.273990723
            print(f'{self.from_value} kilogram(s) is',
                  f'{to_value:,.2f} ounce(s).')
        elif self.from_unit == 'Pound':
            to_value = float(self.from_value) * 16
            print(f'{self.from_value} pound(s) is', 
                  f'{to_value:,.2f} ounce(s).')
        else:
            to_value = float(self.from_value)
            print(f'{self.from_value} ounce(s) is', 
                  f'{to_value:,.2f} ounce(s).')
        return to_value
    
    def to_lb(self):
        '''
        Public method that converts weight units of measurement to pounds.
        '''
        if self.from_unit == 'Gram':
            to_value = float(self.from_value) * 0.0022046244
            print(f'{self.from_value} gram(s) is',
                  f'{to_value:,.2f} pound(s).')
        elif self.from_unit == 'Kilogram':
            to_value = float(self.from_value) * 2.2046244202
            print(f'{self.from_value} kilogram(s) is',
                  f'{to_value:,.2f} pound(s).')
        elif self.from_unit == 'Ounce':
            to_value = float(self.from_value) * 0.0625
            print(f'{self.from_value} ounce(s) is',
                  f'{to_value:,.2f} pound(s).')
        else:
            to_value = float(self.from_value)
            print(f'{self.from_value} pound(s) is',
                  f'{to_value:,.2f} pound(s).')
        return to_value
    
    def to_f(self):
        '''
        Public method that converts temperature units of measurement 
        to fahrenheit.
        '''
        if self.from_unit == 'Celsius':
            to_value = (float(self.from_value) * 1.8) + 32
            print(f'{self.from_value}°C is {to_value:,.2f}°F.')
        else:
            to_value = float(self.from_value)
            print(f'{self.from_value}°F is {to_value:,.2f}°F.')
        return to_value       
    
    def to_c(self):
        '''
        Public method that converts temperature units of measurement 
        to celsius.
        '''
        if self.from_unit == 'Fahrenheit':
            to_value = (float(self.from_value) - 32) * (1/1.8)
            print(f'{self.from_value}°F is {to_value:,.2f}°C.')
        else:
            to_value = float(self.from_value)
            print(f'{self.from_value}°C is {to_value:,.2f}°C.')
        return to_value           
    
    def __update_log(self, value: float):
        '''
        Private method that stores conversions by creating entries in 
        private attribute self.__log (an ordered dictionary).
        '''
        self.__log[(self.category,
                    self.from_value, 
                    self.from_unit)] = ('{:,.2f}'.format(value), 
                                        self.to_unit)
    
    def to_file(self, value: float):
        '''
        Public method that calls private method __update_log(). When a class
        instance calls to_file(), the value returned from a conversion is 
        passed as an argument to to_file() and __update_log(). Entries created 
        to self.__log are written to a text file in append mode.
        '''        
        self.__update_log(value)
        with open('output.txt', 'a') as file:
            utc = datetime.utcnow()
            file.write(f'{utc}  ')
            for k, v in self.__log.items():
                entry = f'{k}: {v}\n'
                file.write(entry)

class Retrieve:
    ''' 
    Class with magic method __getitem__() that reads and prints recent 
    conversions from a text file.
    '''
    def __init__(self, filename):
        ''' 
        Retrieval of data from a text file.
        '''
        self.filename = filename

    def __getitem__(self, index: int):
        ''' 
        Magic method that takes an index as an argument, reads and prints a 
        number of recent conversions up to that index from a text file.
        '''
        try:
            with open(self.filename, 'r') as file:
                content = file.readlines()
                if len(content) < index and len(content) >= 0:
                    for i in range(len(content)):
                        print(content[-(i+1)])
                elif len(content) >= index:
                    for i in range(index):
                        print(content[-(i+1)])
        except FileNotFoundError:
            print('You do not seem to have recents!')