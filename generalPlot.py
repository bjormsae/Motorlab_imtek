import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
channel_one = []
channel_two = []

filename = 'squareWave_04hz'
filepath = 'motorlabData/' + filename + '.csv'
newfilePath = 'plots/' + filename + '.png'

with open(filepath, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        x.append(float(row[0]))
        channel_one.append(float(row[1]))
        channel_two.append(float(row[2]))

x = np.array(x)
x = x - x[0]

print(len(x))


plt.plot(x, channel_one, label='CH1')
plt.plot(x, channel_two, label='CH2')
plt.xlabel("$t$ [s]")
plt.ylabel("$V$ [V]")
plt.legend(loc=2)
plt.savefig(newfilePath)
plt.show()
