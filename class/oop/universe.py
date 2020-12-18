from human import Robot,Human
from planet import Planet

import random

class Universe:
  def __init__(self):
    self.planets = []
     
  def __repr__(self):
    return f"universe)planets ={self.planets})"
  def __str__(self):
    return f"The universe contain {len(self.planets)} planets."
  
  def generate(self,planet):
    planet = Planet()

    for index in range (random.randint(1,10)):
      robot = Robot(f"Robot{index}")
      planet.add_robot(robot)
    
    for index in range(random.randint(1,10)):
      human = Human(f"Human{index}")
      planet.add_human(human)
    
    self.planets.append(planet)
  
  def show_population(self):
    import matplotlib.pyplot as plt
    for i in range(0,len(self.planets),1):
      



if (__name__=="__main__"):
  universe = Universe()
  earth= Planet()
  moon = Planet()
  universe.generate(earth)
  universe.generate(moon)
  print(universe)


  