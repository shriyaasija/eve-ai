import pygame
import sys
from maze import Maze

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("EveAI - Genetic Algorithm Maze Learner")

    clock = pygame.time.Clock()

    maze = Maze(cell_size=40)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)

        maze.draw(screen)

        pygame.display.flip()

        clock.tick(FPS)

    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()