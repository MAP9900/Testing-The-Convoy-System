#Imports
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

#This Program runs 3 simulations testing the probability of a ship/convoy being sighted and graphs the results.

#Simulation Part 1 (One Convoy)

number_of_simulations = 1000
number_of_Uboats = 50 #Can Be Changed
Convoy = (random.uniform(-500, 500), random.uniform(-350, 350)) #Convoy Location Generated at Random.
#Convoy = (-100,50) #Convoy at Fixed Position.
Convoy_radius = 24 #Can Be Changed
results_df = pd.DataFrame(columns=['Simulation #', 'Sightings'])
for test in range(number_of_simulations):
    U_Boat_df_Loc = [(random.uniform(-500, 500), random.uniform(-350, 350)) for _ in range(number_of_Uboats)]
    hits_1 = 0
    for boat in U_Boat_df_Loc:
        distance_squared_1 = (boat[0] - Convoy[0]) ** 2 + (boat[1] - Convoy[1]) ** 2
        if distance_squared_1 <= Convoy_radius ** 2:
            hits_1 += 1
        results_df.loc[test] = [test + 1, hits_1]
average_1 = results_df['Sightings'].mean().__round__(10)
#print(average_1)

#Graph of all 1000 Simulations
plt.figure(figsize=(24,5))
plt.plot(results_df['Simulation #'], results_df['Sightings'], color='#5c919e')
plt.title('Convoy Signtings over 1000 Simulations \n (1 Convoy of 50 Ships)')
plt.xlabel('Simulation Number')
plt.ylabel('Number of U-Boats In Visual Range of Concoy')
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.savefig('Sim_1-1.jpg')
plt.show()


#Histogram
plt.figure(figsize=(8,6))  
plt.hist(results_df['Sightings'], align='mid', color='#5c919e')
plt.xticks(np.arange(0,7,1))
plt.yticks(np.arange(0,1050,50))
plt.title('Histogram of Simulation \n (1 Convoy of 50 Ships)')
plt.ylabel('Times Convoy have been spotted')
plt.xlabel('Number of U-Boats that Sighted the Convoy')
plt.savefig('Sim_1-2.jpg')
plt.show()


#Stimulation Part 2 (50 Indiviual Ships)

num_ships = 50 
Ship_Radius_1 = 6 #Can Be Changed
results_df_2 = pd.DataFrame(columns=['Simulation #', 'Sightings'])
for test_2 in range(number_of_simulations):
    Ship_Loc_1 = [(random.uniform(-500, 500), random.uniform(-350, 350)) for _ in range(num_ships)]
    U_Boat_df_Loc_2 = [(random.uniform(-500, 500), random.uniform(-350, 350)) for _ in range(number_of_Uboats)]
    hits_2 = 0
    for U_Boat_df in U_Boat_df_Loc_2:
        for ship in Ship_Loc_1:
            Ship_center = (ship[0], ship[1])
            distance_squared_2 = (U_Boat_df[0] - Ship_center[0]) ** 2 + (U_Boat_df[1] - Ship_center[1]) ** 2
            if distance_squared_2 <= Ship_Radius_1 ** 2:
                hits_2 += 1
                break
    results_df_2.loc[test_2] = [test_2 + 1, hits_2]
average_2 = results_df_2['Sightings'].mean().__round__(10)
#print(average_2)

#Graph of all 1000 Simulations
plt.figure(figsize=(24,5))
plt.plot(results_df_2['Simulation #'], results_df_2['Sightings'], color='#5c919e')
plt.title('Ship Signtings over 1000 Simulations \n (50 Indiviual Ships)')
plt.xlabel('Simulation Number')
plt.ylabel('Number of U-Boats In Visual Range of a Ship')
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.savefig('Sim_2-1.jpg')
plt.show()


#Histogram
plt.figure(figsize=(8,6)) 
plt.hist(results_df_2['Sightings'], align='mid', color='#5c919e')
plt.xticks(np.arange(0,7,1))
plt.yticks(np.arange(0,1050,50))
plt.title('Histogram of Simulation \n (50 Indiviual Ships)')
plt.ylabel('Times Ships have been spotted')
plt.xlabel('Number of U-Boats that Sighted Ships')
plt.savefig('Sim_2-2.jpg')
plt.show()


#Stimulation Part 3 (Number of Smaller Convoys)

num_convoys = 5 #Can Be Changed
Convoy_radius_2 = 18 #Can Be Changed 
results_df_3 = pd.DataFrame(columns=['Simulation #', 'Sightings'])
for test_3 in range(number_of_simulations):
    convoy_loc = [(random.uniform(-500, 500), random.uniform(-350, 350)) for _ in range(num_convoys)]
    U_Boat_df_Loc_3 = [(random.uniform(-500, 500), random.uniform(-350, 350)) for _ in range(number_of_Uboats)]
    hits_3 = 0
    for U_Boat_df in U_Boat_df_Loc_3:
        for ship in convoy_loc:
            Ship_center_2 = (ship[0], ship[1])
            distance_squared_3 = (U_Boat_df[0] - Ship_center_2[0]) ** 2 + (U_Boat_df[1] - Ship_center_2[1]) ** 2
            if distance_squared_3 <= Convoy_radius_2 ** 2:
                hits_3 += 1
                break
    results_df_3.loc[test_3] = [test_3 + 1, hits_3]
average_3 = results_df_3['Sightings'].mean().__round__(10)
#print(average_3)

#Graph of all 1000 Simulations
plt.figure(figsize=(24,5))
plt.plot(results_df_3['Simulation #'], results_df_3['Sightings'], color='#5c919e')
plt.title('Convoy Signtings over 1000 Simulations \n (5 Convoys of 10 Ships Each)')
plt.xlabel('Simulation Number')
plt.ylabel('Number of U-Boats In Visual Range of a Convoy')
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.savefig('Sim_3-1.jpg')
plt.show()


#Histogram
plt.figure(figsize=(8,6))
plt.hist(results_df_3['Sightings'], align='mid', color='#5c919e')
plt.xticks(np.arange(0,7,1))
plt.yticks(np.arange(0,1050,50))
plt.title('Histogram of Simulation \n (5 Convoys of 10 Ships Each))')
plt.ylabel('Times A Convoy has Been Spotted')
plt.xlabel('Number of U-Boats that Sighted a Convoy')
plt.savefig('Sim_3-2.jpg')
plt.show()


#Stimulation Part 4 (Number of Larger Convoys)

num_convoys = 2 #Can Be Changed
Convoy_radius_3 = 23 #Can Be Changed 
results_df_4 = pd.DataFrame(columns=['Simulation #', 'Sightings'])
for test_4 in range(number_of_simulations):
    convoy_loc_2 = [(random.uniform(-500, 500), random.uniform(-350, 350)) for _ in range(num_convoys)]
    U_Boat_df_Loc_4 = [(random.uniform(-500, 500), random.uniform(-350, 350)) for _ in range(number_of_Uboats)]
    hits_4 = 0
    for U_Boat_df in U_Boat_df_Loc_4:
        for ship in convoy_loc_2:
            Ship_center_3 = (ship[0], ship[1])
            distance_squared_3 = (U_Boat_df[0] - Ship_center_3[0]) ** 2 + (U_Boat_df[1] - Ship_center_3[1]) ** 2
            if distance_squared_3 <= Convoy_radius_3 ** 2:
                hits_4 += 1
                break
    results_df_4.loc[test_4] = [test_4 + 1, hits_4]
average_4 = results_df_4['Sightings'].mean().__round__(10)
#print(average_4)

#Graph of all 1000 Simulations
plt.figure(figsize=(24,5))
plt.plot(results_df_4['Simulation #'], results_df_4['Sightings'], color='#5c919e')
plt.title('Convoy Signtings over 1000 Simulations \n (2 Convoys of 25 Ships Each)')
plt.xlabel('Simulation Number')
plt.ylabel('Number of U-Boats In Visual Range of a Convoy')
for spine in plt.gca().spines.values():
    spine.set_visible(False)
plt.savefig('Sim_4-1.jpg')
plt.show()


#Histogram
plt.figure(figsize=(8,6))
plt.hist(results_df_4['Sightings'], align='mid', color='#5c919e')
plt.xticks(np.arange(0,7,1))
plt.yticks(np.arange(0,1050,50))
plt.title('Histogram of Simulation \n (2 Convoys of 25 Ships Each))')
plt.ylabel('Times A Convoy has Been Spotted')
plt.xlabel('Number of U-Boats that Sighted a Convoy')
plt.savefig('Sim_4-2.jpg')
plt.show()

#Excel File For All 4 Simulations 
#Results = pd.concat([results_df, results_df_2, results_df_3, results_df_4], axis=1, join='inner')
#print(Results)
#with pd.ExcelWriter('____.xlsx') as writer:
    #Results.to_excel(writer)