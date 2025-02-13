"""
Created by Diego Rubio Canales in feb 2025
Universidad Carlos III de Madrid
"""

import numpy as np
from constants import AIR_PRESSURE

# TODO: Implement a method for update preassure

class FluidSimulation:

    def __init__(self, rho: float, mhu: float, p_zero: float, p_gradient: float, Ny: int, Nx: int, height: float, width: float):

        # Density
        self.rho = rho

        # Viscosity
        self.mhu = mhu

         # Dimensions
        self.Ny = Ny    # Number of y-cells     
        self.Nx = Nx    # Number of x-cells

        self.dy = height / Ny   # height must be in meter
        self.dx = width / Nx   # width must be in meter     
        self.dt = 0.001        

        # Origin flow
        self.p_zero = p_zero
        self.p_gradient = p_gradient

        # Velocity field
        self.v = np.zeros((Ny, Nx))   # Vertical
        self.u = np.zeros((Ny, Nx))   # Horizontal

        # Pressure field
        self.p = np.full((Ny, Nx), AIR_PRESSURE)

    def p_matrix(self, Nx, Ny, p_zero):
        """Initial pressure matrix method"""

        # Initialize all the space at ambient pressure
        self.p = np.full((Ny, Nx), AIR_PRESSURE) 

        # Set the position of the gas in first row at a desired position
        self.p[0][Nx//3 :2 * Nx//3]   = p_zero 
    
    def set_preassure_gradient(self, gradient_value):
        """Creates a constant pressure gradient to create a constant flow"""

        # Sets a constant initial preasure zone
        self.p[0][self.Nx//3 :2 * self.Nx//3] = self.p_zero
        
        # Sets a gradient pressure zone for a constant flow
        self.p[1][self.Nx//3 :2 * self.Nx//3] = self.p_zero + gradient_value * 2 * self.dy

    def update_pressure(self):
        """Poisson equation for pressure"""
        # Name simplification
        p = self.p
        rho = self.rho
        u, v = self.u, self.v
        dy, dx, dt = self.dy, self.dx, self.dt


        for i in range(1, len(p) - 1, 1):
            for j in range(1, len(p[i]) - 1, 1):
                # velocity gradient
                v_gradient = (
                    (u[i+1][j] - u[i-1][j]) / 2*dx + 
                    (v[i][j+1] - v[i][j-1]) / 2*dy
                )
                # calculate pressure with poisson equation discretized
                p[i][j] = (
                    (p[i+1][j] + p[i-1][j]) * dy**2 +                   
                    (p[i][j+1] + p[i][j-1]) * dx**2 - 
                    rho * v_gradient * (dx**2) * (dy**2)
                    ) / (2 * ( dx**2 + dy**2))
    def update_walls(self):
        """Sets all the walls as surface with u,v = 0"""
        self.u[0] = self.u[-1] = self.v[0] = self.v[-1] = [0] * self.Nx

    def update_velocity(self):
        """Navier-Stokes momentum equation"""
        # Name simplification
        dx = self.dx
        dy = self.dy
        dt = self.dt
        rho = self.rho
        mhu = self.mhu
        u = self.u
        v = self.v
        p = self.p
        
        for i in range(1, len(u) - 1, 1):
            for j in range(1, len(u[i]) - 1, 1):
                
                #------------------------- u direction -------------------------
                # Doble spacial derivative of u
                doble_grdnt_u = (
                    (u[ i + 1][j] - 2*u[i][j] + u[i-1][j])/dx**2 +  
                    (u[i][j+1] - 2*u[i][j] + u[i][j-1])/dy**2
                )

                # All x direction gradients term for u
                x_grdnt = ((rho * u[i+1][j]**2 + p[i+1][j]) - 
                           (rho * u[i-1][j]**2 + p[i-1][j])) / (2 * dx)
                

                # All y direction grandients term
                y_grdnt = ((rho * u[i][j+1] * v[i][j+1]) - (rho * u[i][j-1] * v[i][j-1])) / (2 * dy)

                # Navier-Stoke momentum equation for u
                u[i][j] = (dt/rho) * (mhu * doble_grdnt_u - x_grdnt - y_grdnt) + u[i][j]

                #------------------------- v direction -------------------------
                # Doble spacial derivative of v
                doble_grdnt_v = (
                    (v[ i + 1][j] - 2*v[i][j] + v[i-1][j])/dx**2 +  
                    (v[i][j+1] - 2*v[i][j] + v[i][j-1])/dy**2
                )

                # All y direction gradients term for v
                v_grdnt = ((rho * v[i][j+1]**2 + p[i][j+1]) - 
                           (rho * v[i][j-1]**2 + p[i][j-1])) / (2 * dy)
                

                # All x direction grandients term
                y_grdnt_v = ((rho * u[i+1][j] * v[i+1][j]) - (rho * u[i-1][j] * v[i-1][j])) / (2 * dx)

                # Navier-Stoke momentum equation for v
                v[i][j] = (dt/rho) * (mhu * doble_grdnt_v - v_grdnt - y_grdnt_v) + v[i][j]


        
        


    


