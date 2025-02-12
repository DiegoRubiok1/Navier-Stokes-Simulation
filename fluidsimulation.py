"""
Created by Diego Rubio Canales in feb 2025
Universidad Carlos III de Madrid
"""
class Fluid:
    def __init__(self, rho: float, mhu: float):

        # Density
        self.__rho = rho

        # Viscosity
        self.__mhu = mhu

