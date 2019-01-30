import json
import requests
import pandas as pd 
from datetime import datetime
import time
import matplotlib.pyplot as plt


#HumanReadableTime to Epoch
def epochtime(x,y):

	import time

	date = x
	time = y
	date_time = date + " " + time
	pattern = '%d-%b-%y %H:%M:%S'
	date_con = datetime.strptime(date_time, pattern)
	epoch = date_con.timestamp()
	return(int(epoch))

#GraphFunction
def AltGraph(df):
	x = df['Date']
	y = df['Altitude']
	plt.style.use(['ggplot','dark_background'])
	plt.xlabel("Date")
	plt.ylabel("Altitude in km")
	plt.title("International Space Station Altitude")
	plt.xticks(rotation = 'vertical', fontsize = "5")
	plt.plot(x,y,'r-o' ,color = 'Red')
	plt.show()

#JsonToDataFrame
def JsonFrame(x):
	response = requests.get(url)
	data = response.json()
	d = pd.DataFrame(data)
	return(d)


#DateTime Data
dt = pd.read_csv("datetime.csv")
length = len(dt)

for i in range (0, length):
	dt["Epoch"][i] = epochtime(dt['Date'][i],dt['Time'][i])


#EpochTimeAddition
dt.to_csv("final.csv")
newdt = pd.read_csv("final.csv")
newdt = pd.DataFrame(newdt)



#Epoch to string
time = ','.join(str(i) for i in newdt['Epoch'] )
time = str(time)


#API CALL & Response
url = "https://api.wheretheiss.at/v1/satellites/25544/positions?timestamps=" + time

d = JsonFrame(url)
newdt['Altitude'] = d['altitude']

print(newdt)
AltGraph(newdt)

############ END CODE ################

