# -*- coding: utf-8 -*-
"""
Li Wen, Stephanie Yow
Class: CS 521 - Spring 1
Date: Sat Feb 14 2025
Final Project
Description: Cooking and Baking Unit Converter (unit_menu.py)
Secondary control enclosed in a function, that ends in the conversion result
or recent conversions being displayed for the user.
"""

import re
import conversion
from collections import OrderedDict

def unit_selection(main_selection: str):
    ''' 
    Function that takes a numeric string (representing the user's selection 
    from the main menu) as an argument. Based on the value passed, the user 
    either proceeds to select their desired units of measurement, input a 
    conversion value and is shown results, or is shown recent conversions.
    '''
    unit_menu = True
    while unit_menu is True:
            
        if main_selection == '1': 
            print('What unit do you wish to convert from?\
                  \nPlease select a number from the menu.\
                  \n1 - Cup\n2 - Tablespoon\n3 - Teaspoon\n4 - Millilitre')
            while True:
                try:
                    from_unit = input('> ')
                    assert from_unit in {'1', '2', '3', '4'}
                    break
                except AssertionError:
                    print('Please enter only one number from 1-4.')

            print('Please enter a value to convert, up to 2 decimal places.')
            while True:
                try:
                    from_value = input('> ')
                    # accept up to 2 decimal places
                    assert re.match(r'^[0-9]+\.?[0-9]?[0-9]?$', from_value)
                    break
                except AssertionError:
                    print('Only numbers up to 2 decimal places are accepted.')
                       
            print('What unit do you wish to convert to?\
                  \nPlease select a number from the menu.\
                  \n1 - Cup\n2 - Tablespoon\n3 - Teaspoon\n4 - Millilitre')
            while True:
                try:
                    to_unit = input('> ')
                    assert to_unit in {'1', '2', '3', '4'}
                    break
                except AssertionError:
                    print('Please enter only one number from 1-4.')
            
            # define category variable
            category = 'Volume'
            
            # dictionary to translate numbered input to worded representation
            # applicable to from_unit and to_unit variables
            volume_menu = OrderedDict([('1', 'Cup'),
                                       ('2', 'Tablespoon'),
                                       ('3', 'Teaspoon'),
                                       ('4', 'Millilitre')
                                       ]
                                      )
            
            # translate from_unit variable
            if from_unit == list(volume_menu.keys())[0]:
                from_unit = list(volume_menu.values())[0]
            elif from_unit == list(volume_menu.keys())[1]:
                from_unit = list(volume_menu.values())[1]
            elif from_unit == list(volume_menu.keys())[2]:
                from_unit = list(volume_menu.values())[2]
            else:
                from_unit = list(volume_menu.values())[3]           
            
            # translate to_unit variable
            if to_unit == list(volume_menu.keys())[0]:
                to_unit = list(volume_menu.values())[0]
            elif to_unit == list(volume_menu.keys())[1]:
                to_unit = list(volume_menu.values())[1]
            elif to_unit == list(volume_menu.keys())[2]:
                to_unit = list(volume_menu.values())[2]
            else:
                to_unit = list(volume_menu.values())[3]                
            
            # instantiate Convert class instance
            convert_volume = conversion.Convert(category, 
                                                from_value, 
                                                from_unit, 
                                                to_unit)
            
            # return, print conversion result and output to file
            if to_unit == list(volume_menu.values())[3]:
                print(convert_volume)
                a = convert_volume.to_ml()
                convert_volume.to_file(a)
            elif to_unit == list(volume_menu.values())[2]:
                print(convert_volume)
                b = convert_volume.to_teaspoon()
                convert_volume.to_file(b)
            elif to_unit == list(volume_menu.values())[1]:
                print(convert_volume)
                c = convert_volume.to_tablespoon()
                convert_volume.to_file(c)
            else:
                print(convert_volume)
                d = convert_volume.to_cup()
                convert_volume.to_file(d)
            
            unit_menu = False
        
        # similar control flow for main_selection values '2' and '3'
        
        elif main_selection == '2':
            print('What unit do you wish to convert from?\
                  \nPlease select a number from the menu.\
                  \n1 - Pound\n2 - Ounce\n3 - Kilogram\n4 - Gram')
            while True:
                try:
                    from_unit = input('> ')
                    assert from_unit in {'1', '2', '3', '4'}
                    break
                except AssertionError:
                    print('Please enter only one number from 1-4.')

            print('Please enter a value to convert, up to 2 decimal places.')
            while True:
                try: 
                    from_value = input('> ')
                    # accept up to 2 decimal places
                    assert re.match(r'^[0-9]+\.?[0-9]?[0-9]?$', from_value)
                    break
                except AssertionError:
                    print('Only numbers up to 2 decimal places are accepted.')
    
            print('What unit do you wish to convert to?\
                  \nPlease select a number from the menu.\
                  \n1 - Pound\n2 - Ounce\n3 - Kilogram\n4 - Gram')
            while True:
                try:
                    to_unit = input('> ')
                    assert to_unit in {'1', '2', '3', '4'}
                    break
                except AssertionError:
                    print('Please enter only one number from 1-4.')
            
            category = 'Weight'
            
            weight_menu = OrderedDict([('1', 'Pound'),
                                       ('2', 'Ounce'),
                                       ('3', 'Kilogram'),
                                       ('4', 'Gram')
                                       ]
                                      )
            
            if from_unit == list(weight_menu.keys())[0]:
                from_unit = list(weight_menu.values())[0]
            elif from_unit == list(weight_menu.keys())[1]:
                from_unit = list(weight_menu.values())[1]
            elif from_unit == list(weight_menu.keys())[2]:
                from_unit = list(weight_menu.values())[2]
            else:
                from_unit = list(weight_menu.values())[3]
            
            if to_unit == list(weight_menu.keys())[0]:
                to_unit = list(weight_menu.values())[0]
            elif to_unit == list(weight_menu.keys())[1]:
                to_unit = list(weight_menu.values())[1]
            elif to_unit == list(weight_menu.keys())[2]:
                to_unit = list(weight_menu.values())[2]
            else:
                to_unit = list(weight_menu.values())[3]                
            
            convert_weight = conversion.Convert(category, 
                                                from_value, 
                                                from_unit, 
                                                to_unit)
                        
            if to_unit == list(weight_menu.values())[3]:
                print(convert_weight)
                a = convert_weight.to_g()
                convert_weight.to_file(a)
            elif to_unit == list(weight_menu.values())[2]:
                print(convert_weight)
                b = convert_weight.to_kg()
                convert_weight.to_file(b)
            elif to_unit == list(weight_menu.values())[1]:
                print(convert_weight)
                c = convert_weight.to_oz()
                convert_weight.to_file(c)
            else:
                print(convert_weight)
                d = convert_weight.to_lb()
                convert_weight.to_file(d)
        
            unit_menu = False            
            
        elif main_selection == '3':
            print('What unit do you wish to convert from?\
                  \nPlease select a number from the menu.\
                  \n1 - Celsius\n2 - Fahrenheit')
            while True:
                try:
                    from_unit = input('> ')
                    assert from_unit in {'1', '2'}
                    break
                except AssertionError:
                    print('Please enter either 1 or 2 only.')

            print('Please enter a value to convert, up to 2 decimal places.')
            while True:
                try: 
                    from_value = input('> ')
                    # accept up to 2 decimal places
                    assert re.match(r'^[0-9]+\.?[0-9]?[0-9]?$', from_value)
                    break
                except AssertionError:
                    print('Only numbers up to 2 decimal places are accepted.')
    
            print('What unit do you wish to convert to?\
                  \nPlease select a number from the menu.\
                  \n1 - Celsius\n2 - Fahrenheit')
            while True:
                try:
                    to_unit = input('> ')
                    assert to_unit in {'1', '2'}
                    break
                except AssertionError:
                    print('Please enter either 1 or 2 only.')
            
            category = 'Temperature'
            
            temp_menu = OrderedDict([('1', 'Celsius'),
                                     ('2', 'Fahrenheit')
                                     ]
                                    )
            
            if from_unit == list(temp_menu.keys())[0]:
                from_unit = list(temp_menu.values())[0]
            else:
                from_unit = list(temp_menu.values())[1]            
            
            if to_unit == list(temp_menu.keys())[0]:
                to_unit = list(temp_menu.values())[0]
            else:
                to_unit = list(temp_menu.values())[1]                
            
            convert_temp = conversion.Convert(category, 
                                              from_value, 
                                              from_unit, 
                                              to_unit)
                        
            if to_unit == list(temp_menu.values())[1]:
                print(convert_temp)
                a = convert_temp.to_f()
                convert_temp.to_file(a)
            else:
                print(convert_temp)
                b = convert_temp.to_c()
                convert_temp.to_file(b)
        
            unit_menu = False                        
        
        elif main_selection == '4':
            # instantiate Retrieve class instance
            recents = conversion.Retrieve('output.txt')
            # print recent 3 conversions
            recents[3]

            unit_menu = False