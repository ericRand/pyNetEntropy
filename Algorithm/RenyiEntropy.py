from Algorithm.AbstractEntropyAlgorithm import *
import math

class RenyiEntropy(AbstractEntropyAlgorithm):

    def __init__(self):
        AbstractEntropyAlgorithm.__init__(self, "renyi")
        self.alpha = 2.7 # for test


    def calculate(self, data):
        self.countCharacters(data)
        sum = 0
        for occurence in self.characters.values():
            sum += (float(occurence) / self.totalCharacters) ** self.alpha
        return ( float(1.0)/(float(1.0)-self.alpha)) * math.log(sum, 2)


