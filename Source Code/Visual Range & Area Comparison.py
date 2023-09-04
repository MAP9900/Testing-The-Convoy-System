#Imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import math

#This program tests the affect of convoy size in relation to visual detection range. 
#Additionally, a comparion of total visual dection area is made to highlight the effectiveness of convoys. 

b = 0.1 #Fraction of the time a ship smokes 
R_1 = 4.0 #Max visual Range of ship, can be changed 
R_2 = 24.0 #Max visual range of smoke, can be changed. Absolute Max = 40
#Sighting range of convoy as a function of size 
results =[]
for x in range(1,61):
    convoy_range = float((R_2 - (1-b)**x * (R_2 - R_1)))
    results.append(convoy_range)
Sighting_df = pd.DataFrame(results)
Sighting_df.rename(columns={0:'Sighting Range'}, inplace=True )
ships = np.arange(1,61).tolist()
Sighting_df['Number of Ships'] = ships
#print(Sighting_df)

#Graph Sighting range of convoy
plt.figure(figsize=(8,6)) 
plt.plot(Sighting_df['Number of Ships'], Sighting_df['Sighting Range'], label='Visual Detection Range')
plt.yticks(np.arange(0, 31, 1))
plt.xticks(np.arange(0, 65, 5))
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.title('Average Visual Range of Convoy Based on Size')
plt.ylabel('Detection Range (Miles)')
plt.xlabel('Convoy Size (Number of Ships)')
plt.axhline(y=R_2, zorder=1, linestyle="--", color="black", label='Maxmim Detection Range (Typical Visual Range of Smoke)')
plt.axhline(y=6, zorder=1, linestyle="--", color="slategrey", label='Minimum Detection Range')
plt.figlegend(loc='center right')
#plt.savefig('Average_Visual_Range.jpg')
plt.show()

#Comparion of Visible Area of Different Convoys 

rows = [0, 4, 9, 14, 19, 29, 59]
Data = Sighting_df.iloc[rows]
Data = Data['Sighting Range']
Areas = []
for x in Data:
    Radius = x
    Area =(math.pi * (Radius**2))
    Areas.append(Area)
factors = [60, 12, 6, 4, 3, 2, 1]
def Total_Area(Areas, factors):
    result = []
    for x, y in zip(Areas, factors):
        result.append(x * y)
    return result
results = Total_Area(Areas, factors)
print(results)

Labels = ['60 Individual Ships', '12 Convoys of 5 Ships', '6 Convoys of 10 Ships', '4 Convoys of 15 Ships', \
          ' 3 Convoys of 20 Ships', '2 Convoys of 30 Ships', '1 Convoy of 60 Ships']
bar_plot = [1, 2, 3, 4, 5, 6, 7]
plt.figure(figsize=(12,6))
plt.bar(bar_plot, results, align='center', width=0.5, color='#5c919e')
plt.title('Comparison of Total Visual Area of Different Convoy Sizes')
plt.xticks(bar_plot, Labels, fontsize=8)
plt.ylabel('Total Visual Detection Area ($\mathregular{Miles^2}$)')
plt.yticks(np.arange(0, 7500, 500))
for spine in plt.gca().spines.values():
    spine.set_visible(False)
#plt.savefig('Area_Comparison.jpg')
plt.show()





