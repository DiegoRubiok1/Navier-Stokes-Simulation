"""
Created by Diego Rubio Canales in feb 2025
Universidad Carlos III de Madrid
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
Nx, Ny = 41, 41  # Grid size
dx, dy = 1.0 / (Nx - 1), 1.0 / (Ny - 1)  # Grid spacing
dt = 0.001  # Time step
nu = 0.1  # Kinematic viscosity
rho = 1.0  # Fluid density

# Initialize velocity and pressure fields
u_field = np.zeros((Nx, Ny))  # Velocity in x
tv = np.zeros((Nx, Ny))  # Velocity in y
p = np.zeros((Nx, Ny))  # Pressure


# Function to compute velocity update
def compute_velocity(u, v, p, dt, dx, dy, nu, rho):
    un = u.copy()
    vn = v.copy()

    # Compute convective terms
    conv_u = un[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[:-2, 1:-1]) / dx + \
             vn[1:-1, 1:-1] * (un[1:-1, 1:-1] - un[1:-1, :-2]) / dy

    conv_v = un[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[:-2, 1:-1]) / dx + \
             vn[1:-1, 1:-1] * (vn[1:-1, 1:-1] - vn[1:-1, :-2]) / dy

    # Compute pressure gradient
    grad_p_x = (p[2:, 1:-1] - p[:-2, 1:-1]) / (2 * dx)
    grad_p_y = (p[1:-1, 2:] - p[1:-1, :-2]) / (2 * dy)

    # Compute viscous diffusion
    viscous_u = nu * (
                (un[2:, 1:-1] - 2 * un[1:-1, 1:-1] + un[:-2, 1:-1]) / dx ** 2 +
                (un[1:-1, 2:] - 2 * un[1:-1, 1:-1] + un[1:-1, :-2]) / dy ** 2)

    viscous_v = nu * (
                (vn[2:, 1:-1] - 2 * vn[1:-1, 1:-1] + vn[:-2, 1:-1]) / dx ** 2 +
                (vn[1:-1, 2:] - 2 * vn[1:-1, 1:-1] + vn[1:-1, :-2]) / dy ** 2)

    # Update velocity field
    u[1:-1, 1:-1] = un[1:-1, 1:-1] - dt * (conv_u + grad_p_x - viscous_u)
    v[1:-1, 1:-1] = vn[1:-1, 1:-1] - dt * (conv_v + grad_p_y - viscous_v)

    return u, v


# Function to update the simulation
def update(frame):
    global u_field, tv, p
    u_field, tv = compute_velocity(u_field, tv, p, dt, dx, dy, nu, rho)
    plt.clf()
    plt.quiver(u_field, tv)  # Display velocity field
    plt.xlim(0, Nx)
    plt.ylim(0, Ny)


# Animation setup
fig = plt.figure()
ani = animation.FuncAnimation(fig, update, frames=200, interval=50)
plt.show()