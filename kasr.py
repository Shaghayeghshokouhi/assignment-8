# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 12:40:25 2023

@author: 2022
"""

def div(f1, f2):
    result = {}
    result['s'] = f1['s'] * f2['m']
    result['m'] = f1['m'] * f2['s']    
    return result

a = {'s': 2, 'm': 5 }
b = {'s': 3, 'm': 7 }

result = div(a,b)
print(result)


def minus(f1, f2):
    result = {}
    result['s'] = (f1['s'] * f2['m']) - (f2['s'] * f1['m'])
    result['m'] = f1['m'] * f2['m']    
    return result

a = {'s': 2, 'm': 5 }
b = {'s': 3, 'm': 7 }

result = minus(a,b)
print(result)