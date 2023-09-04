#Imports
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd
import scipy.stats as stats

#Read in and clean data frame
#file = 'Simulation_Data_(Final).xlsx' #--75 U-Boats
file = 'Simulation_Data_(Final_2).xlsx' #--50 U-Boats
df = pd.read_excel(file)
df.pop(df.columns[0])
#print(df)

#Subplot of Average Sightings
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(8, 7))
bar_plot = [1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
axs[0, 0].bar(bar_plot, df['Average Sightings (1)'])
axs[0, 0].set_title('1 Convoy of 50 Ships')
axs[0, 1].bar(bar_plot, df['Average Sightings (2)'])
axs[0, 1].set_title('50 Indiviual Ships')
axs[1, 0].bar(bar_plot, df['Average Sightings (3)'])
axs[1, 0].set_title('5 Convoys of 10 Ships Each')
axs[1, 1].bar(bar_plot, df['Average Sightings (4)'])
axs[1, 1].set_title('2 Convoys of 25 Ships Each')
plt.yticks(np.arange(0,1.1,0.1))
plt.xticks(np.arange(0,11,1))
fig.supylabel('Percent of Time Convoy Was Spotted')
fig.supxlabel('Simulation Number')
fig.suptitle('Comparison of Average Sighting Percentage \n to Various Sizes of Convoys')
plt.show()
#plt.savefig('Average_Sightings.jpg')

#Relative Loss Rates 
def Sink_Calculations():
    Sim_Number = np.arange(1,11,1)
    df_3 = pd.DataFrame(Sim_Number)
    df_3.rename(columns={0:'Simulation Number'}, inplace=True)
    df_3 = df_3.set_index('Simulation Number')
    sink_percent = 0.40 #About 0.40 of ships hit by a torpedo sunk http://www.ibiblio.org/hyperwar/USN/rep/ASW-51/ASW-FN.html#fn10
    #Simulation 1
    hits_1 = 1.7539375000000001 #Taken Convoy_Sightings.py and is calculation of torpedeo hit when fired at random. 
    escort_1 = 0.447297 #Calculated Escort effect 
    results_1 = []
    for row in df['Average Sightings (1)']:
        sunk_1 = (row * hits_1 * sink_percent * escort_1) 
        results_1.append(sunk_1)
    df_3['Sink Percentage (1)'] = results_1
    #Simualtion 2 (50 Ind. Ships)
    #Ind_sink_percent = random.uniform(0.5, 1.0) #Estimated Sink rate for independnt ships was bewteen 0.5 and 1. 
    Ind_sink_percent = 0.75 #Average of range 0.5 to 1.0
    #Source: http://www.ibiblio.org/hyperwar/USN/rep/ASW-51/ASW-10.html#fig10-5
    escort_2 = 1.161057 #Calculated Escort effect 
    results_2 =[]
    for row in df['Average Sightings (2)']:
        sunk_2 = (row * Ind_sink_percent * escort_2) 
        results_2.append(sunk_2)
    df_3['Sink Percentage (2)'] = results_2
    #Simulation 3
    hits_3 = 1.7539375000000001 #Taken Convoy_Sightings.py and is calculation of torpedeo hit when fired at random. 
    escort_3 = 1.018305 #Calculated Escort effect 
    results_3 = []
    for row in df['Average Sightings (3)']:
        sunk_3 = (row * hits_3 * sink_percent * escort_3) 
        results_3.append(sunk_3)
    df_3['Sink Percentage (3)'] = results_3
    #Simulation 4
    hits_4 = 1.7539375000000001 #Taken Convoy_Sightings.py and is calculation of torpedeo hit when fired at random. 
    escort_4 = 0.804177 #Calculated Escort effect 
    results_4 = []
    for row in df['Average Sightings (3)']:
        sunk_4 = (row * hits_4 * sink_percent * escort_4)
        results_4.append(sunk_4)
    df_3['Sink Percentage (4)'] = results_4
    return df_3
#print(Sink_Calculations())

#SubPlot of Relative Loss Rates
fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(8, 7))
Loss_Rates = Sink_Calculations()
#print(Loss_Rates)
axs[0, 0].bar(bar_plot, Loss_Rates['Sink Percentage (1)'])
axs[0, 0].set_title('1 Convoy of 50 Ships')
axs[0, 1].bar(bar_plot, Loss_Rates['Sink Percentage (2)'])
axs[0, 1].set_title('50 Indiviual Ships')
axs[1, 0].bar(bar_plot, Loss_Rates['Sink Percentage (3)'])
axs[1, 0].set_title('5 Convoys of 10 Ships Each')
axs[1, 1].bar(bar_plot, Loss_Rates['Sink Percentage (4)'])
axs[1, 1].set_title('2 Convoys of 25 Ships Each')
plt.yticks(np.arange(0,1.1,0.1))
plt.xticks(np.arange(0,11,1))
fig.supylabel('Relative Loss Rates')
fig.supxlabel('Simulation Number')
fig.suptitle('Comparison of Relative Loss Rates of \n Various Sizes of Convoys', )
plt.show()
#plt.savefig('Relative_Loss_Rates.jpg')

#Comparisons Of Averages
averages = []
averages.append(Loss_Rates['Sink Percentage (2)'].mean())
averages.append(Loss_Rates['Sink Percentage (3)'].mean())
averages.append(Loss_Rates['Sink Percentage (4)'].mean())
averages.append(Loss_Rates['Sink Percentage (1)'].mean())
#print(averages)

#Plot Of Averages 
plt.figure(figsize=(8,6))
bar_plot_2 = [1, 2, 3, 4]
labels = ['50 Indiviual Ships', '5 Convoys of 10 Ships Each', '2 Convoys of 25 Ships Each', '1 Convoy of 50 Ships']
plt.bar(bar_plot_2, averages, color=['orange', 'green', 'blue', 'red'], label=labels)
plt.xticks(np.arange(1,5,1), color='w')
plt.yticks(np.arange(0,1.1,0.1))
plt.title('Comparison of Average Relative Loss Rates')
plt.xlabel('Convoy Type')
plt.ylabel('Relative Loss Rate')
plt.legend(title='Convoy Type')
plt.show()
#plt.savefig('Average_Relative_Loss_Rate.jpg')


#Anova Test 
data_1 = Loss_Rates['Sink Percentage (1)'].values
data_2 = Loss_Rates['Sink Percentage (2)'].values
data_3 = Loss_Rates['Sink Percentage (3)'].values
data_4 = Loss_Rates['Sink Percentage (4)'].values
f_statistic, p_value = stats.f_oneway(data_1, data_2, data_3, data_4)
#print("F-statistic:", f_statistic)
#print("p-value:", p_value)