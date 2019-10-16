#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 19:40:44 2019

@author: griffin
"""

while True:
    try:
        x = input("First number: ")
        y = input("Second number: ")
        z = int(x)/int(y)
        print(str(z))
    except: 
        print("Please try again.")
    else: 
        break
    