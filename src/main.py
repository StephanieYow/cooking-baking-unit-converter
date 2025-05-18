# -*- coding: utf-8 -*-
"""
Li Wen, Stephanie Yow
Class: CS 521 - Spring 1
Date: Sat Feb 14 2025
Final Project
Description: Cooking and Baking Unit Converter (main.py)
Main control that lets the user select their desired measurement category 
(volume, weight or temperature), get recents, continue, or exit the program. 
"""

import unit_menu

main_menu = True
while main_menu is True:
    print('Welcome! Please select a number from the menu.\
          \n1 - Volume Conversion\n2 - Weight Conversion\
          \n3 - Temperature Conversion\n4 - Get Recents\n5 - Exit')
    while True:
        try:
            main_selection = input('> ')
            assert main_selection in ['1', '2', '3', '4', '5']
            break
        except AssertionError:
            print('Please enter only one number from 1-5.')
    
    if main_selection in ['1', '2', '3', '4']:
        unit_menu.unit_selection(main_selection)
        
        print('Do you want to continue or exit?\
              \nPlease select a number from the menu.\
              \n1 - Continue\n2 - Exit')
        while True:
            try:
                choice = input('> ')
                assert choice in ['1', '2']
                break
            except AssertionError:
                print('Please enter either 1 or 2 only.')
        
        if choice == '1':
            continue
        else:
            main_menu = False
            print('Thank you for using Cooking and Baking Unit Converter!')
        
    else:
        main_menu = False
        print('Thank you for using Cooking and Baking Unit Converter!')