# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 20:12:42 2023

@author: Ogi Wemy
"""

class animal:
    species = "bird"
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
        
parrot = animal("Parrot", 10)
sparrow = animal("sparrow", 15)

print("1. Parrot is a {}".format(parrot.__class__. species))
print("2. Sparrow is also {}".format(sparrow.__class__. species))
print("3. {0} is {1} years old".format(parrot.name, parrot.age))
print("4. {0} is {1} years old".format(sparrow.name, sparrow.age))