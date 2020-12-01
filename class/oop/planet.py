from human import Human
from human import Robot

class Planet:
  def __init__(self):
    self.inhabitants= {'humans':[],'robots':[]}
    
  
  def add_human(self,human):
     self.inhabitants['humans'].append(human)
    
    
    

  def remove_human(self,human):
    self.inhabitants['humans'].remove(human)
    

  def add_robot(self,robot):
    self.inhabitants['robots'].append(robot)
  

  def remove_robot(self,robot):
    self.inhabitants['robots'].remove(robot)
     
  def __repr__(self):
    return f"The list is {self.inhabitants['humans']} and {self.inhabitants['robots']}"

  def __str__(self):
    return f"There are {len(self.inhabitants['humans'])} humans, and {len(self.inhabitants['robots'])} robots"
  
if(__name__ == "__main__"):
  planet = Planet()
  person1 = Human("Darlin")
  person2 = Human("George")
  planet.add_human(person1)
  planet.add_human(person2)
  robot1 = Robot("B12")
  robot2 = Robot("B20")
  planet.add_robot(robot1)
  planet.add_robot(robot2)
  print(planet.__repr__())
  planet.remove_robot(robot1)
  planet.remove_human(person2)
  print(planet.__str__())