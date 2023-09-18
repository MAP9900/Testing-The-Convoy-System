# Testing-The-Convoy-System
Description:
A project based around using data science and WWII era equations to demonstrate the effectiveness of the convoy system. 

OUTLINE OF ALL SOURCE CODE FILES:

1. Convoy sightings.py -- calculates the effect of sonar on ship contacts and the probability of hits and subsequently sinkings. Only hit and sinking probabilities are used in the write up of the project currently. 
2. Real Life Data.py -- Reads in tables web scrapped from 'U-Boat Web Scrape.py' and plots data from http://www.ibiblio.org/hyperwar/USN/rep/ASW-51/ASW-10.html
3. Results of Simulations.py -- Reads in simulation data and plots it. Calculates the relative loss rate and plots this and the averages for each convoy type. Anova test also performed but is not currently relevant to the project.
4. Simulations-Two.py -- Runs all four simulations 10 times each with set seeds and records the outcomes. Exports the outcome as .xlsx file to be used later.
5. Simulations.py -- Same four simulations as in Simulations-Two.py but only runs each once. Plots the outcome of each simulation in a bar chart and histogram.
6. U-Boat Web Scrape.py -- Web Scrapes all the tables from http://www.ibiblio.org/hyperwar/USN/rep/ASW-51/ASW-10.html for use later
7. Visual Range & Area Comparison.py -- Calculates average sighting distance and total visual area and plots both
8. Visualization of 50-1, 2-25 , 5-10.py Plots a visual of the various convoy types
9. Visualization of Convoy (1-50).py -- Plots a visual of one convoy in the North Atlantic
10. Wiki Tables.py -- Web scrapes tables from Wikipedia. Not currently used in the project write up.

Graphs Folder contains all the graphs made from the source code.
