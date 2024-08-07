import os
import math
import numpy as np
import matplotlib.pyplot as plt


arrays = []
file_lens = []
dimension = 40

#Loading binary and converting it to numpy arrays
def file_to_array(directory):
	for files in os.listdir(directory):
		if str(files) == ".DS_Store":
			pass
		else:
			path = directory + "/" + str(files)
			print(str(files))
			print(path)
			with open(path, "r") as file:
				content = file.read()
				content = content.split(" ")
				content.pop(-1)


				sq = math.sqrt(len(content))  #Square rooting length of files (finding dimensions)
				sq = math.floor(sq)           #Rounding down, didn't want values to be annoying floats
				file_lens.append(int(sq))     #Adding ints of values to a list

				for index in range(len(content)):
					content[index] = int(content[index], 2)

				content = content[15:-5]

				array = np.zeros((dimension, dimension))
				counter = 0
				for i in range(dimension):
					for f in range(dimension):
						if counter < len(content):
							array[i, f] = content[counter]
						counter += 1

				arrays.append(array)

	return arrays, file_lens


"""			
directory_Human = "/Users/philipnegrin/Downloads/AICodeDetection/Binary_Human"			
arrays_human, file_lengths_human = file_to_array(directory_Human)
Counter = 0
for array in arrays_human:
	Counter += 1
	plt.imshow(array, cmap="gray")
	path = "/Users/philipnegrin/Downloads/AICodeDetection/training_images/Images_Human" + "/human_code_image" + str(Counter)
	plt.savefig(path)
"""


directory_AI = "/Users/philipnegrin/Downloads/AICodeDetection/Data/Train/AI1"
arrays_ai, file_lengths_AI = file_to_array(directory_AI)
Counter = 0
for array in arrays_ai:
	print(Counter)
	Counter += 1
	plt.imshow(array, cmap="gray")
	path = "/Users/philipnegrin/Downloads/AICodeDetection/Data/Train/AI2" + "/AI_image" + str(Counter)
	plt.savefig(path)


print(file_lens)
print(arrays)







