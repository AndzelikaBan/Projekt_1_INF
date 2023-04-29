# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 20:52:34 2023

@author: andze
"""

import numpy as np
from math import *
from argparse import ArgumentParser

class Transformacje:
    
    # TU MI COS NIE SIEDZI 
    def __init__(self,model):
        if model == "wgs84":
            self.a = 6378137.0 # semimajor_axis
            self.b = 6356752.31424518 # semiminor_axis
        elif model == "grs80":
            self.a = 6378137.0
            self.b = 6356752.31414036
        elif model == "Elipsoida Krasowskiego":
            self.a = 6370245.0
            self.b = 6356863.01877
        else:
            raise NotImplementedError(f"{model} Ta operacja jest niemożliwa!")    
        self.sp = (self.a - self.b) / self.a
        self.e2 = (2 * self.sp - self.sp ** 2) 
        