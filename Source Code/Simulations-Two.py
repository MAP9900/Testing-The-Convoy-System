#Imports
import random
import pandas as pd

#This program runs each simulation ten times for a total of 10,000 tests each. Set seeds are used. 
#Simulations are the exact same as in Simulations.py 

#Seeds 
seeds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Simulation Part 1 (One Convoy)

def simulation_1(seeds):
    random.seed(seeds)
    number_of_simulations = 1000
    number_of_Uboats = 50  #Can Be Changed
    Convoy = (random.uniform(-500, 500), random.uniform(-350, 350))  # Convoy Location Generated at Random.
    # Convoy = (-100,50) #Convoy at Fixed Position.
    Convoy_radius = 24  #Can Be Changed
    results_df = pd.DataFrame(columns=['Simulation #', 'Sightings'])
    for sim in range(number_of_simulations):
        U_Boat_df_Loc = [(random.uniform(-500, 500), random.uniform(-350, 350)) for _ in range(number_of_Uboats)]
        hits_1 = 0
        for boat in U_Boat_df_Loc:
            distance_squared_1 = (boat[0] - Convoy[0]) ** 2 + (boat[1] - Convoy[1]) ** 2
            if distance_squared_1 <= Convoy_radius ** 2:
                hits_1 += 1
        results_df.loc[sim] = [sim + 1, hits_1]
    average_1 = results_df['Sightings'].mean().__round__(10)
    return average_1

#Run Simulation 1
averages_df_1 = pd.DataFrame(columns=['Simulation 1 #', 'Average Sightings (1)'])
for test, seed in enumerate(seeds):
    average_1 = simulation_1(seed)
    averages_df_1.loc[test] = [test + 1, average_1]
#print(averages_df_1)

#Stimulation Part 2 (50 Indiviual Ships)

def simulation_2(seeds):
    random.seed(seeds)
    number_of_simulations = 1000
    number_of_Uboats = 50 #Can Be Changed
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
    return average_2

#Run Simulation 2
averages_df_2 = pd.DataFrame(columns=['Simulation 2 #', 'Average Sightings (2)'])
for test_2, seed in enumerate(seeds):
    average_2 = simulation_2(seed)
    averages_df_2.loc[test_2] = [test_2 + 1, average_2]
#print(averages_df_2)

#Stimulation Part 3 (A Number of Smaller Convoys)

def simulation_3(seeds):
    random.seed(seeds)
    number_of_simulations = 1000
    number_of_Uboats = 50 #Can Be Changed
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
    return average_3

#Run Simulation 3
averages_df_3 = pd.DataFrame(columns=['Simulation 3 #', 'Average Sightings (3)'])
for test_3, seed in enumerate(seeds):
    average_3 = simulation_3(seed)
    averages_df_3.loc[test_3] = [test_3 + 1, average_3]
#print(averages_df_3)

#Stimulation Part 4 (Number of Larger Convoys)

def simulation_4(seeds):
    random.seed(seeds)
    number_of_simulations = 1000
    number_of_Uboats = 50 #Can Be Changed
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
    return average_4

#Run Simulation 4
averages_df_4 = pd.DataFrame(columns=['Simulation 4 #', 'Average Sightings (4)'])
for test_4, seed in enumerate(seeds):
    average_4 = simulation_4(seed)
    averages_df_4.loc[test_4] = [test_4 + 1, average_4]
#print(averages_df_4)

#Excel File For 3 Simulations 
Results = pd.concat([averages_df_1, averages_df_2, averages_df_3, averages_df_4], axis=1, join='inner')
#print(Results)
#with pd.ExcelWriter('Simulation_Data_(Final_2).xlsx') as writer:
    #Results.to_excel(writer)
  