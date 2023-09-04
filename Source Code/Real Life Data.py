#Imports
import matplotlib.pyplot as plt
import numpy as np
import random
import pandas as pd

file = 'Table_3.xlsx'
df = pd.read_excel(file)
file_2 = 'Table_9.xlsx'
df_2 = pd.read_excel(file_2)
file_3 = 'Table_1.xlsx'
df_3 = pd.read_excel(file_3)
#print(df_2)
data = {'Case1': [1, 1], 'Case 2': [0.69, 0.75], 'Case 3': [0.56, 0.55]}
df_results = pd.DataFrame(data)
result = pd.DataFrame(columns=df_results.columns, index=['Product'])
for column in df_results.columns:
    result[column] = df_results[column].product()
#print(result)

#Plotting http://www.ibiblio.org/hyperwar/USN/rep/ASW-51/ASW-10.html#eq2 Calculated Relative Loss Rate
bar_plot = [1, 2, 3]
labels = ['30 Ship Convoy', '60 Ship Convoy', '90 Ship Convoy']
plt.figure(figsize=(8,7))
plt.bar(bar_plot, result.iloc[0], color=['orange', 'green', 'blue'], label=labels)
plt.yticks(np.arange(0, 1.1, 0.1))
plt.xticks(np.arange(1, 4, 1), color='w')
plt.title('Calculated Relative Loss Rate from Report No. 51 \n of the Operations Evaluation Group (1946)')
plt.ylabel('Relative Loss Rate')
plt.xlabel('Convoys')
plt.legend(title='Convoy Size')
plt.show()

#Data from North Atlantic, August 1942 to January 1943:

bar_plot_2 = [1, 2, 3, 4]
labels_2 = ['HX (eastbound 9½ kt)', 'SC (eastbound 7 kt)', 'ON (westbound 9½ kt)', 'ONS (westbound 7 kt']
plt.figure(figsize=(8,7))
plt.bar(bar_plot_2, df_3['Per centconvoyssighted'], color=['orange', 'green', 'blue', 'red'], label=labels_2)
plt.xticks(np.arange(1, 4, 1), color='w')
plt.yticks(np.arange(0, 110, 10))
plt.title('Percent of Convoys Spotted by U-Boats in North Atlantic, \n August 1942 to January 1943')
plt.ylabel('Percent of Convoys Spotted')
plt.xlabel('Convoy Route')
plt.legend(title='Direction')
plt.show()

plt.figure(figsize=(8,7))
plt.bar(bar_plot_2, df_3['Per centshipssunk'], color=['orange', 'green', 'blue', 'red'], label=labels_2)
plt.xticks(np.arange(1, 4, 1), color='w')
plt.yticks(np.arange(0, 11, 1)) 
plt.title('Percent of Ships Sunk by U-Boats in North Atlantic Based on Route, \n August 1942 to January 1943')
plt.ylabel('Percent of Ships Within a Convoy Sunk')
plt.xlabel('Convoy Route')
plt.legend(title='Direction')
plt.show()

#Clean Data from Table 3 and calculate Average Sink rate
#print(df)
column_names = list(df.columns.values)
print("The Column Header :", column_names)
df['Results'] = (df['Averagenumber ofships sunkper attack'] / df['Averagenumber ofships']) * 100
print(df['Results'])

labels_3 = ['0-14', '15-24', '25-34', '35-44', '45-54', '55 and Over']
bar_plot_3 = [1, 2, 3, 4 ,5, 6]
plt.figure(figsize=(8,7))
plt.bar(bar_plot_3, df['Results'], color=['orange', 'green', 'blue', '#f5da42', 'red', 'purple'], \
        label=labels_3)
plt.xticks(np.arange(1, 7, 1), color='w')
plt.yticks(np.arange(0, 110, 10)) 
plt.title('Average Percent of Ships Sunk by U-Boats in North Atlantic \n Based on Convoy Size, 1941-1942')
plt.ylabel('Average Percent of Ships Sunk')
plt.xlabel('Convoy Type')
plt.legend(title='Convoy Size')
plt.show()

