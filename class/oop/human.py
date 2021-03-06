

class Robot:

  # A class attribute
  laws = "Protect, Obey and Survive"

  # A class method
  def the_laws(self):
    print(Robot.laws)

  # An initialiser (special instance method)
  def __init__(self,name):

    # An instance attribute
    self.name = name
    self.age = 0
  def grow(self):
    self.age += 1
  # An instance method
  def display(self):
    print(f"I am {self.name}")
  def __repr__(self):

    return f'robot(name={self.name}, age = {self.age})'
  
  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old.'
  

if (__name__ == "__main__"):
  robot = Robot("groot")
  robot.display()
  robot.grow()
  robot.grow()
  robot.the_laws()
  print(robot)

class Human:
  MAX_ENERGY = 100
  
  def __init__(self,name):
    self.name = name
    self.age = 0
    self.energy= Human.MAX_ENERGY
  
  def grow(self):
    self.age += 1
  
  def eat(self):
    self.energy += 10
    if(self.energy >= Human.MAX_ENERGY):
      print("I'm full, I can no longer eat.")
      self.energy = Human.MAX_ENERGY
    else:
      print("I feel energized")

  
  def move(self):
    if(self.energy == 0):
      print("You died")
      self.energy = 0
    else:
      self.energy -= 10

  def display(self):
    print(f"I am {self.name}")
    
  def __repr__(self):

    return f'human(name={self.name}, age = {self.age})'

  def __str__(self):
    return f'My name is {self.name} and I am {self.age} years old, and my energy is {self.energy}'
  

if(__name__=="__main__"):
  human = Human("Greg")
  human.display()
  human.eat()
  human.grow()
  human.move()
  human.move()
  human.eat()
  print(human)