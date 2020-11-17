import matplotlib.pyplot as plt

def read_data(filepathname):
  with open(filepathname) as file:
    lust = []
    for line in file:
      data = float(line.strip())
      lust.append(data)
    
  file.close()
  return lust

def run():
  data = read_data('visual/subplots/temps.txt')
  
  fig, (ax1, ax2) = plt.subplots(1,2)

  ax1.plot(range(1, 8), data)
  ax2.bar(range(1,8), data)
  plt.tight_layout()
  plt.show()

run()

      
  
