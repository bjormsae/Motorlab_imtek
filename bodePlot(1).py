#Redigeringslogg:
#2022 - Emil Johnsen
#2023 - Emil Johnsen
import matplotlib.pyplot as plt
from tikzplotlib import save as save_tikz

#LEGG INN FREKVENSENE HER
freq_vector = []
#LEGG INN FORSTERKNING I dB HER
amplitude_db_vector = []
#LEGG INN FASEFORSKYVNING I GRADER HER
phase_deg_vector = []

#de følgende linjene lager bodeplot for amplitude og faseforskyvning
fig, (gain_dB,phase_deg) = plt.subplots(2)
fig.suptitle("Bodeplot av forsterkning og faseforskyvning")
gain_dB.plot(freq_vector,amplitude_db_vector)
gain_dB.set_xlabel('$\omega$ [Hz]')
gain_dB.set_xscale('log')
gain_dB.set_ylabel('$K$ [dB]')
phase_deg.plot(freq_vector,phase_deg_vector)
phase_deg.set_xlabel('$\omega$ [Hz]')
phase_deg.set_ylabel('$\psi$ [deg]')
phase_deg.set_xscale('log')
plt.show()

#Dere kan kommentere ut denne linja for å lagre figuren som en latex-figur - Husk at dere da må legge inn hele filstien
#save_tikz('bode_phaser_test.tex')