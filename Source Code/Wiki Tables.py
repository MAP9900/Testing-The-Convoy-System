#Imports
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


url_1 = 'https://en.wikipedia.org/wiki/United_States_home_front_during_World_War_II' #Us War Time Labor Force
#Sources: Bureau of the Census, Historical Statistics of the United States (1976) Chapter D, Labor, Series D 29-41 (Table 1)


url_2 = 'https://en.wikipedia.org/wiki/United_States_aircraft_production_during_World_War_II'

response_1 = requests.get(url_1)
soup_1 = BeautifulSoup(response_1.text,'html.parser')
labor_list_1 = soup_1.find_all('table',attrs={'class':"wikitable"})
labor_df_1 = pd.read_html(str(labor_list_1[0]))[0]
labor_df_2 = pd.read_html(str(labor_list_1[1]))[0]

#Clean labor_df_1
labor_df_1[['Total labor force (*1000)', 'of which Male (*1000)', 'of which Female (*1000)']] = \
labor_df_1[['Total labor force (*1000)', 'of which Male (*1000)', 'of which Female (*1000)']].apply(lambda x: x*1000)
labor_df_1 = labor_df_1.rename(columns={'Total labor force (*1000)': 'Total labor force', 'of which Male (*1000)': 'Male', \
'of which Female (*1000)': 'Female'})                                        

#Clean labor_df_2
labor_df_2[['Armed forces (*1000)', 'Unemployed (*1000)']] = \
labor_df_2[['Armed forces (*1000)', 'Unemployed (*1000)']].apply(lambda x: x*1000)
labor_df_2 = labor_df_2.rename(columns={'Armed forces (*1000)': 'Armed Forces', 'Unemployed (*1000)': 'Unemployed'})
labor_df_2 = labor_df_2.drop(labor_df_2.index[0])

#Graphs
plt.figure(figsize=(10,6))
ax1 = plt.subplot(2,2,1)
plt.plot(labor_df_1['Year'], labor_df_1['Total labor force'], '-o', label='Total Labor Force')
plt.plot(labor_df_1['Year'], labor_df_1['Male'], '-o', label='Male')
plt.plot(labor_df_1['Year'], labor_df_1['Female'], '-o', label='Total Labor Force')
plt.yticks(np.arange(0, 70000000, 10000000))
plt.title('US Labor Force')


ax2 = plt.subplot(2,2,3, sharey=ax1)
plt.plot(labor_df_2['Year'], labor_df_1['Total labor force'], '-o', label='Total Labor Force')
plt.plot(labor_df_2['Year'], labor_df_2['Armed Forces'], '-o', label='Armed Forces')
plt.title

plt.show()