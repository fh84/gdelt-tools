# subsetting GDELT data, a first try 
# Author: FH
# Date: June 24, 2013
# Based on code by David Masad and John Beieler



from IPython.core.display import HTML
styles = open("Style.css").read()
HTML(styles)



import datetime as dt
from collections import defaultdict

import matplotlib.pyplot as plt
import pandas


plt.rcParams['figure.figsize'] = [8,4] # Set default figure size
PATH = "/Users/florianhollenbach/Documents/GDELT_Data/"




data = []
for year in range(1990, 1997):
	f = open(PATH+str(year) +".csv")
	for raw_row in f:
		row = raw_row.split("\t") #split row by tabs
		actor1 = row[5][:3] 
		actor2 = row[15][:3]
		geo_country = row[37]
		geo_lat = row[39]
		geo_long = row[40]
		actor1_name = row[6]
		actor1_type = row[12]
		actor1_ethnic = row[9]
		actor1_rel = row[10]
		actor2_name = row[16]
		actor2_type = row[22]
		actor2_ethnic = row[19]
		actor2_rel = row[20]
		goldstein = row[30]
		quad_codes = row[29] 


		if "ML" in geo_country and ('3' in quad_codes or '4' in quad_codes): # subset location in Mali and confl events
			year = int(row[1][:4])
			month = int(row[1][4:6])
			day = int(row[1][6:])
			quad_cat = row[29]
			data.append([year, month, day, actor1,actor1_name,actor1_type,actor1_ethnic,actor1_rel, actor2,actor2_name,actor2_type,actor2_ethnic,actor2_rel,geo_country,geo_lat,geo_long, quad_cat,goldstein])

print "Mali Conflict Records 1990 - 1997:", len(data)

### make into panda dataframe
Mali_confl_1990_1997 = pandas.DataFrame(data,columns=["Year", "Month", "Day", "Actor1", "Actor1 Name", "Actor1 Type", "Actor1 Ethnic", "Actor1 Religion", "Actor2", "Actor2 Name", "Actor2 Type","Actor2 Ethnic","Actor2 Religion", "Location Country","Latitude","Longitude","QuadCat","Goldstein"])


#now we could export this file as a csv
Mali_confl_1990_1997.to_csv(PATH+"Mali_Confl_1990_1997.csv",sep="," ,na_rep="")
