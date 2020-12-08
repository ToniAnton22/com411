from human import Robot,Human
from planet import Planet

import random

class Universe:
  def __init__(self):
    self.planets = []
    self 
  def __repr__(self):
    return f"universe)planets ={self.planets})"
  def __str__(self):
    return f"The universe contain {len(self.planets)} planets."
  
  def generate(self):
    planet = Planet()

    for index in range (random.randint(1,10)):
      robot = Robot(f"Robot{index}")
      planet.add_robot(robot)
    
    for index in range(random.randint(1,19)):
      human = Human(f"Human{index}")
      human.add_human(human)

if (__name__=="__main__"):
  