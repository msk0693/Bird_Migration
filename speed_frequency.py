import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

birddata = pd.read_csv("bird_tracking.csv")

bird_names = pd.unique(birddata.bird_name)
os.system('clear')

print("Enter the name of a bird from the list below to see the frequency of it's 2D speed. Enter 'quit' to end the program.")
print("-Birds Tracked-")
print(bird_names)
name = input()

while(name != "quit"):
	if(name in bird_names):
		ix = birddata.bird_name == name
		speed = birddata.speed_2d[ix]
		plt.figure(figsize = (8,4))
		plt.title(name + "'s Speed")
		ind = np.isnan(speed)
		plt.hist(speed[~ind], bins = np.linspace(0, 30, 20), density = True)
		plt.xlabel(" 2D speed (m/s) ")
		plt.ylabel(" Frequency ")
		plt.show()

		os.system('clear')
		print("Enter the name of a bird from the list below to see the frequency of it's 2D speed. Enter 'quit' to end the program.")
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







