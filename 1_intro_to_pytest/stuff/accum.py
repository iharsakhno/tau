"""
This module contains a basic accumulator class.
Its purporse is to show how to use pytest framework to testing classes
"""

#-------
# Class: Accumulator
#---------

class Accumulator:
    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self._count

    def add(self, more=1):
        self._count += more