# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:27:23 2026

@author: mikej
"""

from projectilemotion import projectilemotion_solver

angle = 20.0
velocity = 11.0

range_result, height_result = projectilemotion_solver(angle, velocity)

print("Horizontal Distance (Range):", round(range_result, 2), "meters")
print("Maximum Height:", round(height_result, 2), "meters")