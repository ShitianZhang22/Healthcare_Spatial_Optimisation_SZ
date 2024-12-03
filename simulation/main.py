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
        self.start = model.steps  # the time when the patient entered the clinic

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
            duration = self.model.steps - self.start
            print('Patient {} has finished the test. The total duration is {} mins.'.format(self.unique_id, duration))
            self.remove()


class Clinic(mesa.Model):
    def __init__(self, seed=None):
        super().__init__()
        self.grid = mesa.space.MultiGrid(7, 1, False)
        self.duration = [1, 5, 2, 16, 5, 0, 1]

    def gen_patient(self):
        """
        Generate and place a new patient at the entrance
        """
        a = Patient(self)
        self.grid.place_agent(a, (0, 0))

    def step(self):
        """Advance the model by one step."""
        print(self.steps)
        if self.steps % 5 == 1:
            self.gen_patient()
        self.agents.do('step')


if __name__ == '__main__':
    clinic = Clinic()
    for t in range(100):
        # print(t)
        clinic.step()
