import matplotlib.pyplot as plt
import csv
import numpy as np

x = []
channel_one = []
channel_two = []

filename1 = 'H_P_r'
filepath = 'motorlabData/' + filename1 + '.csv'
newfilePath = 'plots/' + filename1 + '.png'

with open(filepath, 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        x.append(float(row[0]))
        channel_one.append(float(row[1]))

filename2 = 'H_P_m'
filepath = 'motorlabData/' + filename2 + '.csv'


with open(filepath, 'r') as csvfile2:
    plots2 = csv.reader(csvfile2, delimiter=',')
    for row in plots2:
        channel_two.append(float(row[1]))

x = np.array(x)
x = x - x[0]

print(len(x))

j = 12500
k = 7500
plt.plot(x[:j-k], channel_one[k:j], label='CH1')
plt.plot(x[:j-k], channel_two[k:j], label='CH2')
plt.xlabel("$t$ [s]")
plt.ylabel("$V$ [V]")
plt.legend(loc=2)
plt.savefig(newfilePath)
plt.show()
