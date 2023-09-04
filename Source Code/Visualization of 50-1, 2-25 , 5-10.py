#Imports
import matplotlib.pyplot as plt
from collections import OrderedDict
from matplotlib.lines import Line2D   
import numpy as np
import random
import pandas as pd

#This program is a visualization of three variations of convoy size. 

#Visulization Of 50 Individual Ships

#random.seed(10)
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
ship_df = pd.DataFrame(columns=['X (Ship)', 'Y (Ship)'])
ship_x = []
ship_y = []
for _ in (range(50)):
    loc_x = random.randint(-500,500)
    loc_y = random.randint(-350,350)
    ship_x.append(loc_x)
    ship_y.append(loc_y)
ship_df['X (Ship)'] = ship_x
ship_df['Y (Ship)'] = ship_y

plt.figure(figsize=(8, 6), facecolor='0.7')
ax = plt.gca()
for _, ship in ship_df.iterrows():
    x, y, = ship['X (Ship)'], ship['Y (Ship)']
    Ship_obj = plt.Circle((x, y), 6, edgecolor='b', facecolor='none', linestyle='-', label='Ship')
    ax.add_patch(Ship_obj)
plt.scatter(U_Boat_df['X'], U_Boat_df['Y'], color='black', s=2, label="U-Boat")
plt.gca().set_facecolor('Teal')
plt.grid(linestyle='--', linewidth=0.5)
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
legend1 = Line2D([], [], color="white", linestyle='none', marker='o', markersize=5, markerfacecolor="black")
legend2 = Line2D([], [], color="white", linestyle='none', marker='o', markersize=6,  markeredgecolor="Blue")
plt.legend((legend1, legend2),('U-Boat', 'Ship'), loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Visualization of Random U-Boat VS Ship Distribution in North Atlantic \n (50 Individual Ships)')
plt.yticks(np.arange(-350, 400, 50))
plt.xticks(np.arange(-500, 550, 50), rotation=45)
plt.ylabel('Miles')
plt.xlabel('Miles') 
for spine in plt.gca().spines.values():
    spine.set_visible(False)
#plt.savefig('Visulization_50-1.jpg')
plt.show()



#Visulization Of 2 Covoys of 25 Ships

#random.seed(10)
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
ship_df = pd.DataFrame(columns=['X (Ship)', 'Y (Ship)'])
ship_x = []
ship_y = []
for _ in (range(2)):
    loc_x = random.randint(-500,500)
    loc_y = random.randint(-350,350)
    ship_x.append(loc_x)
    ship_y.append(loc_y)
ship_df['X (Ship)'] = ship_x
ship_df['Y (Ship)'] = ship_y
#Graph
plt.figure(figsize=(8, 6), facecolor='0.7')
ax = plt.gca()
for _, ship in ship_df.iterrows():
    x, y, = ship['X (Ship)'], ship['Y (Ship)']
    Ship_obj = plt.Circle((x, y), 23 , edgecolor='b', facecolor='none', linestyle='-', label='Ship')
    ax.add_patch(Ship_obj)
plt.scatter(U_Boat_df['X'], U_Boat_df['Y'], color='black', s=2, label="U-Boat")
plt.gca().set_facecolor('Teal')
plt.grid(linestyle='--', linewidth=0.5)
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
legend3 = Line2D([], [], color="white", linestyle='none', marker='o', markersize=5, markerfacecolor="black")
legend4 = Line2D([], [], color="white", linestyle='none', marker='o', markersize=15,  markeredgecolor="Blue")
plt.legend((legend3, legend4),('U-Boat', 'Convoy'), loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Visualization of Random U-Boat VS Convoy Distribution in North Atlantic \n (2 Convoys of 25 Ships Each)')
plt.yticks(np.arange(-350, 400, 50))
plt.xticks(np.arange(-500, 550, 50), rotation= 45)
plt.ylabel('Miles')
plt.xlabel('Miles') 
for spine in plt.gca().spines.values():
    spine.set_visible(False)
#plt.savefig('Visulization_2-25.jpg')
plt.show()


#Visulization Of 5 Covoys of 10 Ships

#random.seed(10)
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
ship_df = pd.DataFrame(columns=['X (Ship)', 'Y (Ship)'])
ship_x = []
ship_y = []
for _ in (range(5)):
    loc_x = random.randint(-500,500)
    loc_y = random.randint(-350,350)
    ship_x.append(loc_x)
    ship_y.append(loc_y)
ship_df['X (Ship)'] = ship_x
ship_df['Y (Ship)'] = ship_y
#Graph
plt.figure(figsize=(8, 6), facecolor='0.7')
ax = plt.gca()
for _, ship in ship_df.iterrows():
    x, y, = ship['X (Ship)'], ship['Y (Ship)']
    Ship_obj = plt.Circle((x, y), 18 , edgecolor='b', facecolor='none', linestyle='-', label='Ship')
    ax.add_patch(Ship_obj)
plt.scatter(U_Boat_df['X'], U_Boat_df['Y'], color='black', s=2, label="U-Boat")
plt.gca().set_facecolor('Teal')
plt.grid(linestyle='--', linewidth=0.5)
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
legend3 = Line2D([], [], color="white", linestyle='none', marker='o', markersize=5, markerfacecolor="black")
legend4 = Line2D([], [], color="white", linestyle='none', marker='o', markersize=15,  markeredgecolor="Blue")
plt.legend((legend3, legend4),('U-Boat', 'Convoy'), loc='center left', bbox_to_anchor=(1, 0.5))
plt.title('Visualization of Random U-Boat VS Convoy Distribution in North Atlantic \n (5 Convoys of 10 Ships Each)')
plt.yticks(np.arange(-350, 400, 50))
plt.xticks(np.arange(-500, 550, 50), rotation= 45)
plt.ylabel('Miles')
plt.xlabel('Miles') 
for spine in plt.gca().spines.values():
    spine.set_visible(False)
#plt.savefig('Visulization_5-10.jpg')
plt.show()
