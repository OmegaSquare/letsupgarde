# -*- coding: utf-8 -*-
"""OTP-PROGRAM_PYTHON-PROJECT.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EzOnLBUVrj1buGMPRIwQ7WQrqCAvmAdE
"""

import random as r
import string 
length = 8
temp = ''
char = string.ascii_letters + string.digits

for i in range(length):
   temp = temp + r.choice(char)


   
print("Your unique One-Time-Password: ", temp)