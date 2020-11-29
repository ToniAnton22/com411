import matplotlib.pyplot as plt

def read_data():
  temps= {}
  import csv
  with open('visual/subplots/temps.csv') as csv_file:
   
    csv_reader = csv.reader(csv_file, delimiter = ',', quotechar = '"')
    header = next(csv_reader)
    
    header = header[0].split()
   
    rebmun = []
    number = []
    for row in csv_reader:
      row =row[0].split()
      
      number.append(float(row[0]))
      rebmun.append(float(row[1]))
    
   
    temps[header[0]] = number
    temps[header[1]] = rebmun
  

  return temps

def run():
  data = read_data()
  first = data['week1']
  second = data['week2']
  first = [int(i) for i in first]
  second = [int(i) for i in second]

  
  fig, (ax1, ax2) = plt.subplots(1,2)

  ax1.plot(range(len(data['week1'])), data['week1'])
  ax2.plot(range(len(data['week2'])), data['week2'])
  plt.show()

  plt.set_xlable("Days")
  plt.set_ylable("Temperature")
  plt.tight_layout()
  plt.show()

run()


      