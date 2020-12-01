from human import Human
from human import Robot

class Planet:
  def __init__(self):
    self.humans = []
    self.robots = []
    self.hr = []
  
  def add_human(self,human):
    self.humans.append(human)
    
    

  def remove_human(self,human):
    self.humans.remove(human)
    

  def add_robot(self,robot):
    self.robots.append(robot)
  

  def remove_robot(self,robot):
    self.robots.remove(robot)
     

  def __repr__(self):
    return f"The list of humans is: {self.humans}\n,and the list of robots is {self.robots}" 

  def __str__(self):
    return f"The list of humans is: {self.humans}\n,and the list of robots is {self.robots}" 
  
if(__name__ == "__main__"):
  planet = Planet()
  person1 = Human()
  person2 = Human()
  person1 = "Darlin"
  person2 = "George"
  planet.add_human(person1)
  planet.add_human(person2)
  robot1 = Robot()
  robot2 = Robot()
  robot1 = "B20"
  robot2 = "B12"
  planet.add_robot(robot1)
  planet.add_robot(robot2)
  print(planet.__repr__())
  planet.remove_robot(robot1)
  planet.remove_human(person2)
  print(planet.__str__())