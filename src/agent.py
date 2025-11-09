import pygame
import random

class Agent:
    def __init__(self, start_pos, max_moves=50):
        self.start_x, self.start_y = start_pos
        self.x = self.start_x
        self.y = self.start_y

        self.moves = [random.randint(0, 3) for _ in range(max_moves)]
        self.current_move = 0

        self.is_alive = True
        self.reached_goal = False

        self.fitness = 0

    def reset(self):
        """Reset agent to starting position"""
        self.x = self.start_x
        self.y = self.start_y
        self.current_move = 0
        self.is_alive = True
        self.reached_goal = False

    def update(self, maze):
        """Execute next move"""
        if not self.is_alive or self.reached_goal:
            return
        
        if self.current_move >= len(self.moves):
            self.is_alive = False
            return
        
        # get next move
        direction = self.moves[self.current_move]
        self.current_move += 1

        # calculate new position
        new_x, new_y = self.x, self.y

        if direction == 0: #up
            new_y -= 1
        elif direction == 1:
            new_x += 1
        elif direction == 2:
            new_y += 1
        elif direction == 3:
            new_x -= 1

        # check if new position is valid 
        if maze.is_wall(new_x, new_y):
            self.is_alive = False
        else:
            self.x = new_x
            self.y = new_y

            if (self.x, self.y) == maze.goal_pos:
                self.reached_goal = True

    def draw(self, screen, cell_size):
        """Draw the agent"""
        if not self.is_alive:
            return
        
        colour = (0, 0, 255)

        pixel_x = self.x * cell_size + cell_size // 2
        pixel_y = self.y * cell_size + cell_size // 2

        pygame.draw.circle(screen, colour, (pixel_x, pixel_y), cell_size // 3)