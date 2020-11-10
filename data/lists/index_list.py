
def movements():
  path = ["Move Forward",10,"Move Backwards",5, "Turn Left",3, "Turn Right",1]
  print(path)
  return(path)

def run():
  print("Moving....")
  path = movements()
  print("{} for {} steps".format(path[0], path[1]))
  print("{} for {} steps".format(path[2], path[3]))
  print("{} for {} steps".format(path[4], path[5]))
  print("{} for {} steps".format(path[6], path[7]))

run()