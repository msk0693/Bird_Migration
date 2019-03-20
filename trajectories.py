import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

birddata = pd.read_csv("bird_tracking.csv")

bird_names = pd.unique(birddata.bird_name)
os.system('clear')

print("Enter the name of a bird from the list below to see it's trajectory. Enter 'all' to see all the birds trajectories. Enter 'quit' to end the program.")
print("-Birds Tracked-")
print(bird_names)
name = input()

while(name != "quit"):
	if(name == "all"):
		plt.figure(figsize = (7,7))
		plt.title(" Gull Trajectories ")
		for bird_name in bird_names:
			ix = birddata.bird_name == bird_name
			x,y = birddata.longitude[ix], birddata.latitude[ix]
			plt.plot(x,y,".", label=bird_name)
		plt.xlabel("Longitude")
		plt.ylabel("Latitude")
		plt.legend(loc="lower right")
		plt.show()
		os.system('clear')
		print("Enter the name of a bird from the list below to see it's trajectory. Enter 'all' to see all the birds trajectories. Enter 'quit' to end the program.")
		print("-Birds Tracked-")
		print(bird_names)
		name = input()
	elif(name in bird_names):
		ix = birddata.bird_name == name
		x,y = birddata.longitude[ix], birddata.latitude[ix]
		plt.figure(figsize = (7,7))
		plt.plot(x,y,"b.")
		plt.title(name + "'s Trajectory")
		plt.xlabel("Longitude")
		plt.ylabel("Latitude")
		plt.show()
		os.system('clear')
		print("Enter the name of a bird from the list below to see it's trajectory. Enter 'all' to see all the birds trajectories. Enter 'quit' to end the program.")
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






