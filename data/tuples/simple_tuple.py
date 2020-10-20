def likelihood():
  likelihoods = (50,38,27,99,4)
  return likelihoods

def run():
  likelihoods = likelihood()
  print("Minimum likelihood of falling: {}%".format(min(likelihoods)))

run()
