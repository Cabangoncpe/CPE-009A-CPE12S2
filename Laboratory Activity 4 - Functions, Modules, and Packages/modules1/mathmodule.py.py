# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 20:20:45 2026

@author: mikej
"""

import math

def quadratic_formula(a,b,c):
    if b**2-(4*a*c)<0: # involving imaginary numbers
        x1 = (complex(-b,math.floor(math.sqrt(abs(b**2-(4*a*c))))))/2*a
        x2 = (complex(-b,-1*math.floor(math.sqrt(abs(b**2-(4*a*c))))))/2*a
        return x1, x2
    else:
        x1 = (-b+math.sqrt(b**2-(4*a*c)))/(2*a)
        x2 = (-b-math.sqrt(b**2-(4*a*c)))/(2*a)
        return x1, x2

#print(quadratic_formula(1,12,32))
print(quadratic_formula(1,2,3))