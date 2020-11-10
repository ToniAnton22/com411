def observed():
  observations=[]
  for count in range(5):
    num = input()
    observations.append(num)
  return observations

def remove_observations(observations):
  delet = ''
  while delet != 'no':
      delet = input("Do you wish to delete one observation?(yes/no)")
      if delet == 'yes':
        item = input("What item do you wish to delete?")
        observations.remove(item)
        print("Done! You have removed an observation")
      else:
        print("Done!")

  
def run():
  observations = observed()
  remove_observations(observations)
  observations_set= set()
  for observation in observations:
    occurences = observations.count(observation)
    observations_set.add((observation,occurences))
  #sorted sorts the set and gives you back a different set
  for key, value in sorted(observations_set):
    print(f"{key} observed {value} times.")

run()