import random
from agent import Agent

class Population:
    def __init__(self, maze, population_size=50, max_moves=50):
        self.maze = maze
        self.population_size = population_size
        self.max_moves = max_moves
        self.generation = 1

        self.agents = []
        for _ in range(population_size):
            agent = Agent(maze.start_pos, max_moves)
            self.agents.append(agent)
        
        self.current_agent_index = 0
        self.all_dead = False

    def update(self):
        """update all agents in the population"""
        all_finished = True

        for agent in self.agents:
            if agent.is_alive and not agent.reached_goal:
                agent.update(self.maze)
                all_finished = False

        self.all_dead = all_finished

    def is_generation_complete(self):
        """check is all agents are done"""
        return self.all_dead
    
    def get_best_agent(self):
        """get the agent with the best fitness"""
        if not self.agents:
            return None
        return max(self.agents, key=lambda a: a.fitness)

    def reset_population(self):
        """reset all agents to starting position"""
        for agent in self.agents:
            agent.reset()
        self.all_dead = False