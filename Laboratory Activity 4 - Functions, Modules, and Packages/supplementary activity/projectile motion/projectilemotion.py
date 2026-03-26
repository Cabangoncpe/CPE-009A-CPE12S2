# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:15:20 2026

@author: mikej
"""

import math

def projectilemotion_solver(angle_deg, velocity):
    g = 9.8  # gravity (m/s^2)

    angle_rad = math.radians(angle_deg)

    # Range formula
    R = (velocity**2 * math.sin(2 * angle_rad)) / g

    # Maximum height formula
    h = (velocity**2 * (math.sin(angle_rad))**2) / (2 * g)

    return R, h