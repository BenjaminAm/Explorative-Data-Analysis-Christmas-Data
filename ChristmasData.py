# -*- coding: utf-8 -*-
"""
Created on Sat Mar 03 12:58:24 2018

@author: Benni
"""

import numpy as np

naughty_nice_2016 = np.array([False, False, True, True, False, True, False, True, False,
True, True, True, True, True, False, True, True, True, True, False, True, True, 
True, True, True, True, True, True, True, False, False, True, True, True, True, True,
False, True, False, True, True, True, True, False, True, True, True, False, False,
 True, True, False, True, True, False, True, True, False, True, True, True, True, True,
True, True, False, True, False, True, True, True, True, False, False, True, True, 
False, True, True, True, True, True, False, True, True, True, True, True, True, True,
True, True, True, True, False, True, True, True, True, True], dtype=bool)

naughty_nice_2017 = np.array([ True, True, True, True, False, False, True, True, 
                              False, False, True, True, True, True, True, True, 
                              True, True, False, True, True, False,
                              False, True, True, True, False, True, True, True, 
                              True, True, True, True, True, True, False, True, 
                              True, True, False, True, False, True, 
                              True, False,True, False, True, True, True, True, 
                              True, True, True, True, True, False, True, False,
                              True, True, True, True, False, True, 
                              True, True, True, True, False, True, True, True, 
                              True, True, True, True, False, True, True, True, 
                              True, False, True, True, True, False, 
                              False, True, True, True, True, False, False, True, 
                              True, True, True, True], dtype=bool)

#A
result = 0
for item in naughty_nice_2016:
    if item == True:
        result = result + 1
    
print(result)

#B
result = 0
naughty_as_list = naughty_nice_2016.tolist()
for index, item in enumerate(naughty_as_list):
    if naughty_nice_2017[index] == naughty_nice_2016[index]:
        result = result + 1
    
print(result)

#C
result = 0
naughty_as_list = naughty_nice_2016.tolist()
for index, item in enumerate(naughty_as_list):
    if naughty_nice_2017[index] == False and naughty_nice_2016[index] == False:
        result = result + 1
    
print(result)

#D
result = 0
naughty_as_list = naughty_nice_2016.tolist()
for index, item in enumerate(naughty_as_list):
    if naughty_nice_2017[index] == False and naughty_nice_2016[index] == True:
        result = result + 1
    if naughty_nice_2017[index] == True and naughty_nice_2016[index] == False:
        result = result + 1
    
print(result)

#E
result = 0
naughty_as_list = naughty_nice_2016.tolist()
for index, item in enumerate(naughty_as_list):
    if naughty_nice_2017[index] == True and naughty_nice_2016[index] == False:
        result = result + 1
    
print(result)

#F
# the string is encoded with caesar cipher, key is 5 (look at %)
frostai_output = 'Wthpns,%wtzsi%ymj%Hmwnxyrfx%ijhnxnts%ywjj&'
decoded_output = ""
for char in frostai_output:
    decoded_output = decoded_output + chr(ord(char) - 5) #ord() returns ASCII value, chr() converts back to char

print(decoded_output)