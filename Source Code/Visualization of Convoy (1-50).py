#Imports
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D      
import numpy as np
import random
import pandas as pd
import math

#This program is a visualization of a convoy in the Mid-Atlantic

#random.seed(10)
Convoy = (-100,50)
data_x = []
data_y = []
for boat in (range(50)):
    location_x = random.randint(-500,500)
    location_y = random.randint(-350,350)
    data_x.append(location_x)
    data_y.append(location_y)
U_Boat_df = pd.DataFrame(data_x)
U_Boat_df['Y'] = data_y
U_Boat_df.rename(columns={0:'X'}, inplace=True)
Boat_number = np.arange(1,51).tolist()
U_Boat_df['U-Boat'] = Boat_number
U_Boat_df = U_Boat_df.set_index('U-Boat')
#print(U_Boat_df.head())
plt.figure(figsize=(8, 6), facecolor='0.7')
ax = plt.gca()
plt.scatter(U_Boat_df['X'], U_Boat_df['Y'], color='black', s=2, label='U-Boat')
circle = plt.Circle((Convoy[0], Convoy[1]), 25, color='Blue', fill=False, label='Convoy')
plt.gca().add_artist(circle)
plt.gca().set_facecolor('Teal')
plt.grid(linestyle='--', linewidth=0.5)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
legend1 = Line2D([], [], color="white", linestyle='none', marker='o', markersize=5, markerfacecolor="black")
legend2 = Line2D([], [], color="white", linestyle='none', marker='o', markersize=16,  markeredgecolor="Blue")
plt.legend((legend1, legend2),('U-Boat', 'Convoy'), loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Visualization of Random U-Boat Distribution in North Atlantic')
plt.yticks(np.arange(-350, 400, 50))
plt.xticks(np.arange(-500, 550, 50), rotation= 45)
plt.ylabel('Miles')
plt.xlabel('Miles') 
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.show()
#plt.savefig('Visualization_1-50.jpg')





 


