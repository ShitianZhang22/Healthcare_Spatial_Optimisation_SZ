"""
version 1.0
TOY MODEL
"""

import mesa
import numpy as np


class Patient(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.stay = 1  # the remaining time a patient is forced at the current cell

    def step(self):
        if self.stay == 0:
            self.move()
        else:
            self.stay -= 1
            print('Patient {} is at {}.'.format(self.unique_id, self.pos[0]))

    def move(self):
        new_pos = self.pos[0] + 1
        if new_pos < self.model.grid.width:
            self.model.grid.move_agent(self, (new_pos, 0))
            self.stay = self.model.duration[new_pos]
            print('Patient {} is at {}.'.format(self.unique_id, self.pos[0]))
        else:
            print('Patient {} has finished the test.'.format(self.unique_id))
            self.remove()


class Clinic(mesa.Model):
    def __init__(self, seed=None):
        super().__init__()
        self.grid = mesa.space.MultiGrid(7, 1, False)
        self.duration = [1, 5, 2, 16, 5, 0, 1]

        # Create agents
        for _ in range(1):
            self.gen_patient()

    def gen_patient(self):
        """
        Generate and place new patients at the entrance
        """
        a = Patient(self)
        self.grid.place_agent(a, (0, 0))

    def step(self):
        """Advance the model by one step."""

        self.agents.do('step')


if __name__ == '__main__':
    clinic = Clinic()
    for _ in range(100):
        print(_)
        clinic.step()
