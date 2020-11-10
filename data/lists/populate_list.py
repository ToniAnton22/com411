def directions():
  direction= ["Move Forward", "Move Backward", "Turn Left","Turn Right"]
  return direction

def menu():
  print("Please select a direction:")
  direction = directions()

  for i in range(0, len(direction), 1):
    print(i, ":",direction[i])
  user_input= int(input())
  direction = direction[user_input]
  return direction

def run():
  route = []
  print("Working out escape route...")
  
  while len(route) < 5:
    direction = menu()
    route.append(direction)
  print("Escape route: ", route)

run()