def directions():
  direction= ["Move Forward", "Move Backward", "Turn Left","Turn Right"]
  return direction

def menu():
  print("Please select a direction:")
  direction = directions()

  for i in range(0, len(direction), 1):
    print(i, ":",direction[i])

def run():
  menu()

run()

