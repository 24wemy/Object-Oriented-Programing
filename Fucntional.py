# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 20:05:14 2023

@author: Ogi Wemy
"""

species = "bird"

def bird_parrot(name, age):
    print("3. {0} is {1} years old".format(name, age))
    

def bird_sparrow(name, age):
    print("4. {0} is {1} years old".format(name, age))
    
    
print("1.Parrot is a {}".format(species))
print("2.Sparrow is also {}".format(species))

bird_parrot("parrot", 10)
bird_sparrow("sparrow", 15)