"""
Created by Diego Rubio Canales in feb 2025
Universidad Carlos III de Madrid
"""
from fluid import Fluid

#IN PROCESS: Getting the physics and math interpretation of Navier-Stokes

class Simulation:
    def __init__(self, nx: int, ny: int, dy: float, dx: float, dt: float,
                 fluid: Fluid):

        # Grid parameters
        self.__nx = nx
        self.__ny = ny

        # Numerical approximation parameters
        self.__dx = dx
        self.__dy = dy
        self.__dt = dt

        # Fluid instance
        self.fluid = fluid




if __name__ == '__main__':
    pass
