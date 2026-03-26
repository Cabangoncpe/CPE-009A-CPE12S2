# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:29:07 2026

@author: mikej
"""

import math

def quadratic_solver(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        result = f"Two real roots: {root1}, {root2}"

    elif discriminant == 0:
        root = -b / (2*a)
        result = f"One real root: {root}"

    else:
        result = "No real roots"

    with open("quadratic_output.txt", "w") as file:
        file.write(f"Equation: {a}x^2 + {b}x + {c} = 0\n")
        file.write(result)
    return result

if __name__ == "__main__":
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    print(quadratic_solver(a, b, c))