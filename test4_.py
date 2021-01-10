"""importing all libraries"""
import time
import pandas as pd
import numpy as np

with open('subset_elemets.txt') as f:
    subset_elements = f.read().split('\n')
    
with open('all_elements.txt') as f:
    all_elements = f.read().split('\n')
 """starting the clock"""   
start = time.time()
verified_elements = set()
"""adding elements to verified elements"""
for element in subset_elements:
    verified_elements.add(element)

print(len(verified_elements))
"""calculating duration of  intersection of two arrays"""
print('Duration: {} seconds'.format(time.time() - start))

print(len(verified_elements))
print('Duration: {} seconds'.format(time.time() - start))
