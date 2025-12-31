import pygame
import sys
from maze import Maze
from population import Population

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("AdamAI - Genetic Algorithm Maze Learner")
    clock = pygame.time.Clock()
    
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)
    
    maze = Maze(cell_size=40)
    population = Population(maze, population_size=50, max_moves=100)
    
    # Control simulation
    show_all_agents = True
    frame_counter = 0
    frames_per_move = 2  # Start a bit faster to see evolution
    mutation_rate = 0.01  # 1% mutation rate
    auto_evolve = True  # Automatically create next generation
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    population.reset_population()
                    print("Population reset!")
                elif event.key == pygame.K_SPACE:
                    show_all_agents = not show_all_agents
                    print(f"Show all agents: {show_all_agents}")
                elif event.key == pygame.K_UP:
                    frames_per_move = max(1, frames_per_move - 1)
                    print(f"Speed: {frames_per_move} frames per move")
                elif event.key == pygame.K_DOWN:
                    frames_per_move += 1
                    print(f"Speed: {frames_per_move} frames per move")
                elif event.key == pygame.K_e:
                    # Manual evolution trigger
                    if population.is_generation_complete():
                        population.evolve(mutation_rate)
                elif event.key == pygame.K_a:
                    # Toggle auto-evolution
                    auto_evolve = not auto_evolve
                    print(f"Auto-evolve: {auto_evolve}")
        
        # Update population
        frame_counter += 1
        if frame_counter >= frames_per_move:
            frame_counter = 0
            if not population.is_generation_complete():
                population.update()
            elif auto_evolve:
                # Automatically evolve when generation completes
                population.evolve(mutation_rate)
        
        # Draw everything
        screen.fill(WHITE)
        maze.draw(screen)
        
        # Draw agents
        if show_all_agents:
            for agent in population.agents:
                if agent.is_alive:
                    pixel_x = agent.x * maze.cell_size + maze.cell_size // 2
                    pixel_y = agent.y * maze.cell_size + maze.cell_size // 2
                    pygame.draw.circle(screen, GRAY, (pixel_x, pixel_y), 3)
        else:
            best_agent = population.get_best_agent()
            if best_agent and best_agent.is_alive:
                best_agent.draw(screen, maze.cell_size)
        
        # Draw status
        alive_count = sum(1 for a in population.agents if a.is_alive)
        best_agent = population.get_best_agent()
        best_fitness = best_agent.fitness if best_agent else 0
        
        status_text = f"Gen: {population.generation} | Alive: {alive_count}/{population.population_size} | Best: {best_fitness:.3f}"
        text = font.render(status_text, True, BLACK)
        screen.blit(text, (10, 10))
        
        # Instructions
        instructions = [
            "SPACE: Toggle view (all/best)",
            "UP/DOWN: Speed control",
            "A: Toggle auto-evolve",
            "E: Evolve manually",
        ]
        y_offset = 50
        for instruction in instructions:
            inst_text = small_font.render(instruction, True, BLACK)
            screen.blit(inst_text, (10, y_offset))
            y_offset += 25
        
        # Speed and auto-evolve indicator
        speed_text = small_font.render(f"Speed: {frames_per_move} | Auto: {auto_evolve}", True, BLACK)
        screen.blit(speed_text, (10, y_offset + 10))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()