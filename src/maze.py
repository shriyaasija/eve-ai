import pygame

class Maze:
    def __init__(self, cell_size=40):
        self.cell_size = cell_size

        self.grid = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]

        self.start_pos = (1, 1)
        self.goal_pos = (8, 5)

        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    def draw(self, screen):
        WALL_COLOUR = (50, 50, 50)
        PATH_COLOUR = (200, 200, 200)
        START_COLOUR = (0, 255, 0)
        GOAL_COLOUR = (255, 0, 0)

        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.cell_size
                y = row * self.cell_size

                if self.grid[row][col] == 1:
                    colour = WALL_COLOUR
                else:
                    colour = PATH_COLOUR
                
                pygame.draw.rect(screen, colour, (x, y, self.cell_size, self.cell_size))

                pygame.draw.rect(screen, (100, 100, 100),
                                 (x, y, self.cell_size, self.cell_size), 1)
                
        start_x = self.start_pos[0] * self.cell_size
        start_y = self.start_pos[1] * self.cell_size
        pygame.draw.rect(screen, START_COLOUR, 
                        (start_x, start_y, self.cell_size, self.cell_size))
        
        goal_x = self.goal_pos[0] * self.cell_size
        goal_y = self.goal_pos[1] * self.cell_size
        pygame.draw.rect(screen, GOAL_COLOUR,
                         (goal_x, goal_y, self.cell_size, self.cell_size))
        
    def is_wall(self, x, y):
        """Check if a grid position is a wall"""
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
            return True
        return self.grid[y][x] == 1
        