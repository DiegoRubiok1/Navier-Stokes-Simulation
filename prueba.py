from fluidsimulation import FluidSimulation


simulation = FluidSimulation(1, 1, 10.6, -20, 10, 10, 1, 1)

# prints the origin preassure
print(simulation.p)

simulation.p_matrix(simulation.Nx, simulation.Ny, simulation.p_zero)
print(simulation.p)

simulation.set_preassure_gradient(simulation.p_gradient)
print(simulation.p)

for i in range(3):
    simulation.set_preassure_gradient(simulation.p_gradient)

    simulation.update_velocity()
    print(simulation.u)
