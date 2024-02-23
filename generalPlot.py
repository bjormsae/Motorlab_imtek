import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
channel_one = []
channel_two = []

filename = 'instrumenteringsforsterker_gain'
filepath = 'motorlabData/' + filename + '.csv'
newfilePath = 'plots/' + filename + '.png'

with open(filepath, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        x.append(float(row[0]))
        channel_one.append(float(row[1]))
        channel_two.append(float(row[2]))

print(len(x))


plt.plot(x, channel_one, label='CH1')
plt.plot(x, channel_two, label='CH2')
plt.legend()
plt.savefig(newfilePath)
plt.show()
