# Creating a program that allows the user
# to chose between different bands,albums and finally
# songs
print("Chose between the following artists, by typing their name, or type \"random song\" to play a random song from the artist: ")

band = input("Breaking Benjamin \nTheory of a Deadman\n")

if band == 'Breaking Benjamin':
  print("Which album would you like to play?")
  album = input("Ember\nDark Before Dawn\nPhobia\n")

  if album == 'Ember' or album == 'ember':
    print("Chose between the following songs:")
    song = input("Red cold river\nBlood\nFeed the Wolf\n")

    if song == 'Red cold river' or song =='Red Cold River':
      print("Playing \"Red cold river\" by Breaking Benjamin")

    elif song == 'Blood' or song =='blood':
      print("Playing \"Blood\" by Breaking Benjamin")

    elif song == 'Feed the Wolf' or song =='feed the wolf':
      print("Playing \"Feed the Wolf\" by Breaking Benjamin")

    else:
      print("Sorry, this is not part of the album")
  
  elif album == 'Dark Before Dawn' or album == 'dark before dawn':
    print("Chose between the following songs: ")
    song = input("Angels Fall\nThe Great Divide\nBreaking the Silence\n")

    if song == 'Angels Fall' or song == 'angels fall':
      print("Playing \"Angels Fall\" by Breaking Benjamin")

    elif song == 'The Great Divide' or song =='the great divide':
      print("Playing \"The Great Divide\" by Breaking Benjamin")

    elif song == 'Breaking the Silence' or song =='breaking the silence':
      print("Playing \"Breaking the Silence\" by Breaking Benjamin")

    else:
      print("We don't have that song here.")
      

  elif album == 'Phobia' or album == 'phobia':
    print("Chose between the following songs:")
    song = input("Diary of Jane\nUnknown Soldier\nEvil Angel\n")

    if song == 'Diary of Jane' or song =='diary of jane':
      print("Playing \"Diary of Jane\" by Breaking Benjamin")

    elif song == 'Unknown Soldier' or song == 'unknown soldier':
      print("Playing \"Unknown Soldier\" by Breaking Benjamin")

    elif song == 'Evil Angel' or song== 'evil angel':
      print("Playing \"Evil Angel\" by Breaking Benjamin")

    else:
      print("We don't have that song here.")

if band == 'Theory of a Deadman':
  print("Which album would you like to play?")
  album = input("Say Nothing\nWake Up Call\n")

  if album == 'Say Nothing' or album == 'say nothing':
    print("Chose between the following songs:")
    song = input("World Keeps Spinning\nBlack Hole In Your Heart\nHistory of Violence\n")

    if song == 'World Keeps Spinning' or song =='world keeps spinning':
      print("Playing \"World Keeps Spinning\" by Breaking Benjamin")

    elif song == 'Blakc Hole In Your Heart' or song == 'black hole in your heart':
      print("Playing \"Black Hole In Your Heart\" by Breaking Benjamin")

    elif song == 'History of Violence' or song =='history of violence':
      print("Playing \"History of Violence\" by Breaking Benjamin")

    else:
      print("Sorry, this is not part of the album")
  
  elif album == 'Wake Up Call' or album == 'wake up call':

    print("Chose between the following songs:")
    song = input("Straight Jacket\nRx(medicate)\nTime Machine\n")

    if song == 'Straight Jacket' or song =='straight jacket':
      print("Playing \"Straight Jacket\" by Breaking Benjamin")

    elif song == 'Rx(medicate)' or song =='rx(medicate)':
      print("Playing \"rx(medicate)\" by Breaking Benjamin")

    elif song == 'Time Machine' or song =='time machine':
      print("Playing \"Time Machine\" by Breaking Benjamin")

    else:
      print("We don't have that song here.")

elif band == 'random':
  print("Type the name of the band and ,enter, and then type \"random\" and we will play you a random song: ")

  band= input("Chose band: ")
  song = input("Type random: ")

  if band == 'Breaking Benjamin' and song == 'random':
   print("Playing a random song from Breaking Benjamin.")

  elif band == 'Theory of a Deadman' and song == 'random':

    print("Playing a random song from Breaking Benjamin.")

else:
  print("Download more songs")
    


  