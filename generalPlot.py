import matplotlib.pyplot as plt
import csv
import os
print(os.getcwd())

x = []
channel_one = []
channel_two = []

filename = 'sineWave_02hz'
filepath = 'motorlabData/' + filename + '.csv'
newfilePath = 'plots/' + filename + '.png'

with open(filepath, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        x.append(row[0])
        channel_one.append(row[1])
        channel_two.append(row[2])

print(len(x))

x = x[:200]
channel_one =channel_one[:200]
channel_two =channel_two[:200]

plt.plot(x, channel_one, label='CH1')
plt.plot(x, channel_two, label='CH2')
plt.legend()
plt.savefig(newfilePath)
plt.show()
