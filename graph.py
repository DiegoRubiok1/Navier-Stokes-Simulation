"""
Created by Diego Rubio Canales in feb 2025
Universidad Carlos III de Madrid
"""

from fluidsimulation import FluidSimulation
import pygame

class Graph:
    """Graphical implement of a 2d cage with water"""
    def __init__(self):
        
        # Fluid simulation instance
        self.simulation = FluidSimulation(
            rho=1000, mhu=0.001, 
            p_zero=10, v_gradient=-100, 
            Ny=100, Nx=100, 
            height=1, width=1
            )
        # Initial pressure matrix
        self.simulation.p_matrix(
            self.simulation.Nx, self.simulation.Ny, self.simulation.p_zero
            )
        
        # Pygame initialize
        pygame.init()

        # Clock instance
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

        # Resolution and frame rate
        self.fps = 30
        self.dimension = (800, 800)

        # Pygame screen initialize
        self.screen = pygame.display.set_mode(self.dimension)
        pygame.display.set_caption("Fluid simulation")

    
    def handle_events(self):
        """Handle de events in screen."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def update(self):
        """Actualize the logic of the simulation."""

        # Set the walls with velocity 0
        self.simulation.update_walls()

        # Pressure gradient zone actualize
        self.simulation.velocity_gradient(self.simulation.v_gradient)

        # Update pressure grid
        self.simulation.update_pressure()

        # Update velocity grid
        self.simulation.update_velocity()

        

    def draw(self):
        """Draws elements in screen"""

        self.screen.fill((0, 0, 0))  # black screen
        self.draw_grid()
        pygame.display.update()      # refresh


    def draw_grid(self):
        """Draws the pressure grid with  pixel squares"""
        for i in range(len(self.simulation.v)):
            for j in range(len(self.simulation.v[i])):

                # y-velocity(u) and x-velocity(v)
                v = self.simulation.v[i][j]
                u = self.simulation.u[i][j]

                # Red color for velocity
                color = ( 
                    self.__normalize_v_to_255(u+v), # Red
                    0,  # Green
                    0   # Blue
                    )
                
                # Calculate size of each square
                size = self.dimension[0] // self.simulation.Nx 

                pos = (size*j + 1, size*i + 1)  # Position
                rect = (pos[0], pos[1], size-1, size-1) #rect object

                # Draw rectangle
                print(color)
                pygame.draw.rect(self.screen, color, rect)
    
    def __normalize_v_to_255(self, v: float) -> float:
        """Normalize velocity value in the range of [0, 255]"""

        max_v = 4 * self.simulation.v_gradient * self.simulation.dy
        min_v = 0

        return abs(255 * (v - min_v)/(max_v - min_v))
     

    def run(self):
        """Executes the main loop."""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.fps)
        pygame.quit()


if __name__ == "__main__":
    graph = Graph()
    graph.run()



