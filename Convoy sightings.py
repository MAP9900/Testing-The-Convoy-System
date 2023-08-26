#Imports
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
import math


#Sonar Part 1 - Visualization of detection range
results_2 = []
for y in range(1,171):
    sonar_range = y**(1/3)
    results_2.append(sonar_range)
ships_2 = np.arange(1,171).tolist()
plt.figure(figsize=(8,6))
plt.plot(ships_2, results_2)
plt.grid(linestyle='--', linewidth=0.5)
plt.yticks(np.arange(0,6,0.5))
plt.xlabel('Number of Ships')
plt.ylabel('Factor by which Detection Range Increases')
plt.title('Visualization of Sonar Detection Range')
plt.show()
#plt.savefig('Sonar_1.jpg')

#Sonar Part 2 - Visualization of predicted number of sonar contacts
results_3 = []
for y in range(1,171):
    sonar_range = y**(2/3)
    results_3.append(sonar_range)
plt.figure(figsize=(8,5))
plt.plot(ships_2, results_3)
plt.yticks(np.arange(0,32,2))
plt.xlabel('Number of Ships', fontsize=12)
plt.ylabel('Factor by which Number of Sonar Detections \n Decreases on a Given Number of Ships', loc='center', fontsize=11)
plt.title('Predicted Number of Sonar Contacts as a \n Function of Number of Ships')
plt.grid(linestyle='--', linewidth=0.5)
plt.show()
#plt.savefig('Sonar_2.jpg')

#Effect of Convoys

file ='Table_6.xlsx'
df = pd.read_excel(file)
#Best Fit line for Escort 
linearCoefficients = np.polyfit(df['Mean escortstrength'], df['Ships sunk perU-boat in pack'], 1)
xFit = np.linspace(0, 15, 16)
yFit = np.polyval(linearCoefficients, xFit)
X_Y_Data = pd.DataFrame(columns=['X Points', 'Y Points'])
X_Y_Data['X Points'] = xFit
X_Y_Data['Y Points'] = yFit
print(X_Y_Data)

plt.figure(figsize=(8,6))
plt.scatter(df['Mean escortstrength'], df['Ships sunk perU-boat in pack'], label='WWII Data Points')
plt.plot(xFit, yFit, color='Black', label='Best Fit Line')
plt.legend()
plt.grid(linestyle='--', linewidth=0.5)
plt.xticks(np.arange(0, 16, 1))
plt.yticks(np.arange(0, 1.6, 0.1))
plt.title('Sinkings Compared to Number of Escorts')
plt.ylabel('Sinkings Per U-Boat Attack')
plt.xlabel('Number of Escorts')
plt.show()
#plt.savefig('Escort_Effect.jpg')

#Probability of a Torpedo Hit on Convoy
l = 140 #Length of Ship (Yards)
L = 800 #Length of Column (Yards)
c = 3 #Number of Columns the torpedo can pass through (5000 yd range, fired from 2000 yd equals 3 columns given \ 
#1000 yds between each column)
prob = (1-(1-l/L)**c) #Probability of hit of one torpedoe 
hits = []
sinkings = []
for z in range(1,6): #Slavo of 1 to 5 torpedoes fired
    salvo = (prob * z)
    hits.append(salvo)
for v in hits:
    sunk = (v * 0.40) #About 0.40 of ships hit by a torpedo sunk http://www.ibiblio.org/hyperwar/USN/rep/ASW-51/ASW-FN.html#fn10
    sinkings.append(sunk)
bar_plot = [1, 2, 3, 4, 5]
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(12, 6))
ax1.bar(bar_plot, hits)
ax2.bar(bar_plot, sinkings)
ax1.set_ylabel('Torpedo Hit Rate', fontsize='14')
ax2.set_ylabel('Sink Rate', fontsize='14')
plt.yticks(np.arange(0,3.1,0.5))
plt.xticks(np.arange(1,6,1))
fig.supxlabel('Number of Torpedos Fired', fontsize='12')
fig.suptitle('Torpedos Hits and Subsequent Sinkings \n as a Function of Number of Torpedos Fired ')
plt.show()
#plt.savefig('Prob_of_Sink.jpg')

