# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:44:35 2026

@author: mikej
"""

name = "Royce Chua"
file = open("newfile1.txt",'w')
file.write(f"Hello, {name}!\n")
file.write("Isn't this amazing!\n")
file.write("that we can create and write on text files\n")
file.write("using Python.")
file.close()