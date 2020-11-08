def search(books_seq):
  print("Searching...")
  data = {}

  with open("data/files/txt/books_seq.txt") as file:
    sections = ""
    for line in file:
      if (line.startswith("Section")):
        parts = line.split(":")
        sections = parts[1].strip()
      elif (sections in data):
        data[sections].append(line.strip())
      else:
        data[sections] = [line.strip()]
    
  print("Done!")
  return data

def run():
  data = search("data/files/txt/books_seq.txt")

  with open("data/files/txt/generate.csv", "w") as file:
    for section, books in data.items():
      for book in books:
        file.write(f"{section},{book}\n")

run()