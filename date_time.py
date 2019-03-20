import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
import os


birddata = pd.read_csv("bird_tracking.csv")
bird_names = pd.unique(birddata.bird_name)
timestamps = []
for k in range(len(birddata)):
	timestamps.append(datetime.datetime.strptime(birddata.date_time.iloc[k][:-3], "%Y-%m-%d %H:%M:%S")) #Year-Month-Date and Hour-Minute-Second format
os.system('clear')
print("Enter the name of a bird from the list below to see the distance its covered. Enter 'quit' to end the program.")
print("-Birds Tracked-")
print(bird_names)
name = input()

while(name != "quit"):
	if(name in bird_names):
		if(name == "Eric"):
			ix = 0
		elif(name == "Nico"):
			ix = 19795
		else:
			ix = 40916
		birddata["timestamp"] = pd.Series(timestamps, index = birddata.index)
		#Time elapsed since the beginning of data collection.
		times = birddata.timestamp[birddata.bird_name == name]
		elapsed_time = [time-times[ix] for time in times]
	
		#Plot
		plt.plot(np.array(elapsed_time)/datetime.timedelta(days=1))
		plt.title(name + "'s Time and distance ")
		plt.xlabel(" Observation ")
		plt.ylabel(" Elapsed time (days) ")
		plt.show()

		os.system('clear')
		print("Enter the name of a bird from the list below to see the distance its covered. Enter 'quit' to end the program.")
		print("-Birds Tracked-")
		print(bird_names)
		name = input()
	else:
		os.system("clear")
		print("No bird named: " + name + ". Enter a name listed below.")
		print("-Birds Tracked-")
		print(bird_names)
		name = input()

print("END OF LINE")



