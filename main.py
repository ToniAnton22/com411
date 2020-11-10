def gang():
  print("Loading gang...")
  friends = []
  friends.append("Scooby Doo")
  friends.append("Shaggy Rogers")
  friends.append("Fred Jones")
  friends.append("Daphne Blake")
  friends.append("Velma Dinkley")
  print(friends)
  print("Done!")
  return friends

gang()

def phrases(friends):
  quotes = {}
  for friend in friends:
    print(f"What does {friend} say?")
    quote = input()
    quotes[friend] = quote
  return quotes

friends = gang()
quotes = phrases(friends)
print(f"Phrases: {quotes}\n")

def save(quotes):
 
  with open("data/files/txt/quotes.txt", "w") as file:
    for friend in quotes:
      quote = quotes[friend]
      file.write(f"{str(friend)}: {str(quote)} \n")


save(quotes)
print("The file contains...")
file = open("data/files/txt/quotes.txt")
print(file.read())
file.close()
