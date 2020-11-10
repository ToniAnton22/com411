def steps():
  likelihoods=("step 1", 50),("step 2", 38),("step 3", 27),("step 4", 99),("step 5", 4)
  return likelihoods

def run():
  likelihoods=steps()
  good_steps = []
  bad_steps = []
  good = int
  bad = int
  for i in range(0,len(likelihoods),1):
    if likelihoods[i] >= :
     bad +=1 
     bad_steps.append(likelihoods[i])
    else:
      good +=1
      good_steps.eppend(likelihoods[i])

  return print("Good steps:",good,"Bad steps:",bad)

run()



