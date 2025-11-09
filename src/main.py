import pygame
import sys
from maze import Maze
from agent import Agent

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("EveAI - Genetic Algorithm Maze Learner")
    clock = pygame.time.Clock()

    font = pygame.font.Font(None, 36)

    maze = Maze(cell_size=40)
    agent = Agent(maze.start_pos, max_moves=100)

    # control simulation speed
    frame_counter = 0
    frames_per_move = 10 

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: # press R to reset
                    agent.reset()
                    print("Agent reset!")
        
        frame_counter += 1
        if frame_counter >= frames_per_move:
            frame_counter = 0
            agent.update(maze)
            print(f"Move {agent.current_move}: Position ({agent.x}, {agent.y}), Alive: {agent.is_alive}, Goal: {agent.reached_goal}")

        screen.fill(WHITE)
        maze.draw(screen)
        agent.draw(screen, maze.cell_size)

        # draw debug text
        status = "GOAL!" if agent.reached_goal else ("DEAD" if not agent.is_alive else "ALIVE")
        text = font.render(f"Move: {agent.current_move}/100 | Status: {status}", True, BLACK)
        screen.blit(text, (10, 10))
        
        # instructions
        small_font = pygame.font.Font(None, 24)
        instructions = small_font.render("Press R to reset", True, BLACK)
        screen.blit(instructions, (10, 50))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()