def search(locations):
  print("Searching...")
  with open("data/files/txt/locations.txt") as file:
    for lines in file:
      print("Looked into {}".format(lines), end='')
      lines = file.readline(4)

  print("\n...Done!")

def run():
  search("data/files/txt/locations.txt")


run()