#Imports 
from bs4 import BeautifulSoup
import requests
import pandas as pd

#This Program web scrapes all the graphs off Chapter 10 in OEG report 51 for use in later analysis.

url_1 = 'http://www.ibiblio.org/hyperwar/USN/rep/ASW-51/ASW-10.html#fig10-5'
URL2 ='https://www.ibiblio.org/hyperwar/USN/Admin-Hist/011-Convoy/011-Convoy-3.html' #Not Used!

results_1=requests.get(url_1)
doc = BeautifulSoup(results_1.text, "html.parser")
tables_1 = doc.find_all('table')
table_1 = pd.read_html(str(tables_1[11]))[0] #TABLE 1. Convoy losses in North Atlantic, August 1942 - January 1943. 
table_2 = pd.read_html(str(tables_1[17]))[0] #TABLE 2. Losses for convoys on northerly routes.
table_3 = pd.read_html(str(tables_1[18]))[0] #TABLE 3. Losses for various sizes of convoys, 1941-1942 \
#(North Atlantic Allied convoys - wolf-pack attacks)
table_4 = pd.read_html(str(tables_1[20]))[0] #TABLE 4. Sinkings from Japanese convoys as a function of size.
table_5 = pd.read_html(str(tables_1[22]))[0] #TABLE 5. Frequency of attacks and sinkings as a function of convoy size. \
#(1942-1943, Western North Atlantic)
table_6 = pd.read_html(str(tables_1[25]))[0] #TABLE 6. Merchant ship losses as a function of escort strength. \
#(1941-1942 in North Atlantic).
table_7 = pd.read_html(str(tables_1[29]))[0] #TABLE 7. Ship losses as a function of air escort. \
#(August to December 1942, North Atlantic).
table_8 = pd.read_html(str(tables_1[32]))[0] #TABLE 8. Comparison of convoy sizes.
table_9 = pd.read_html(str(tables_1[33]))[0] #TABLE 9. Relative loss rates.
#print(table_9)
#with pd.ExcelWriter('Table_1.xlsx') as writer:
    #table_1.to_excel(writer)
