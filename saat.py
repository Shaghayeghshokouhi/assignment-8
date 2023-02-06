# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 13:17:02 2023

@author: 2022
"""

def minus(t1, t2):
    result = {}
    result['h'] = t1['h'] - t2['h']
    result['m'] = t1['m'] - t2['m']
    result['s'] = t1['s'] - t2['s']
    
    if result['s'] < 0:
        result['m'] -= 1
        result['s'] += 60
        
            
    if result['m'] < 0:
        result['m'] += 60
        result['h'] -= 1
        
        
    return result

t1 = {"h": 5, "m": 45, "s": 40}  
t2 = {"h": 2, "m": 30, "s": 86}


result = minus(t1,t2)
print(result)