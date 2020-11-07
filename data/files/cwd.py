def cwd():
  import os
  path = os.getcwd()
  
  print(f"Current Working Directory: {path}")
  for file in os.listdir(path):
    print(file)

def run():
  print("Processing....")
  cwd()

run()