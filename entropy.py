# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="eric"
__date__ ="$6 mars 2014 14:54:44$"

import math
import zlib


def count_characters(data):
    characters = {}
    totalCharacters = 0

    for i in data:
        totalCharacters += 1
        if i in characters:
            characters[i] = characters[i] + 1
        else:
            characters[i] = 1
        
    return characters, totalCharacters

def shannon_entropy(data):
    characters, totalCharacters = count_characters(data)
    entropy = 0
    for occurence in characters.values():
        frequency = float(occurence) / totalCharacters
        if frequency > 0:
            entropy += frequency * math.log(frequency,2)
    return -entropy

# Reasonable approximation to the Kolmogorov Complexity
# using the compression rate
# ref.: http://lorenzoriano.wordpress.com/tag/python/
def kolmogorov_complexity(data):
    l = float(len(data))
# avoiding division by 0
    if l != 0:
        compr = zlib.compress(data)
        c = float(len(compr))
        return c/l
    else:
        return 0