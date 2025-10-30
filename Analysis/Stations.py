import numpy as np

class Station_obj:
    def __init__(self, name, times, velocities , min, max, mean):
        self.name = name
        self.times = times
        self.velocities = velocities
        self.max = max
        self.min = min
        self.mean = mean

    def __str__(self):
        return f"Station:{self.name} \n Minimum_velocity: {self.min} \n Mean_velocity: {self.mean} \n Maximum_velocity: {self.max}"