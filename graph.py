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
            p_zero=10, p_gradient=-1, 
            Ny=100, Nx=100, 
            height=1, width=1
            )
        
        # Pygame initialize
        pygame.init()
        self.screen = pygame.display.set_mode((100, 100))
        pygame.display.set_caption("Fluid simulation")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.fps = 3

    
    def handle_events(self):
        """Handle de events in screen."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def update(self):
        """Actualize the logic of the simulation."""
        pass

    def draw(self):
        """Draws elements in screen"""
        pass

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



