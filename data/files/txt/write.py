def search(books):
  print("Searching...")
  sections = []
  book = []
  with open("data/files/txt/books.txt") as file:

    for lines in file:
     
    
     if lines.startswith("Section"):
      
        b = lines.split(":")[1]
        sections.append(b.strip())
        
     
     else:
       book.append(lines.strip())
       
 
  
  print("Done!")
  return (sections, book) 

def save(books, data):
  print("Saving...")
  data = search(books)
  with open("data/files/txt/books.txt", "w") as file:
    file.write("Section: {}".format(data))
    file.write("Books: {}".format(data))
    
 
      
def run():
  data = search("data/files/txt/books.txt")
  save("data/files/txt/books.txt",data)

run()