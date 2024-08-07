import os
from BinaryFileConverter import read_file_as_binary, write_binary_to_file

AI_train_path = "/Users/philipnegrin/Downloads/AICodeDetection/Data/Train/AI1"
AI_test_path = "/Users/philipnegrin/Downloads/AICodeDetection/Data/Test/AI1"

human_train_path = "/Users/philipnegrin/Downloads/AICodeDetection/Data/Train/Human"
human_test_path = "/Users/philipnegrin/Downloads/AICodeDetection/Data/Test/Human"

split_point = "3873"

counter_AI = 0
counter_human = 0
data_path = "/Users/philipnegrin/Downloads/AICodeDetection/APPS/test"
if_start = False
for folder_path in os.listdir(data_path):
	if folder_path == ".DS_Store":
		pass
	else:
		new_path = os.path.join(data_path, folder_path)
		print(new_path)
		if new_path[-4:] == "3873":
			if_start = True
		if if_start:
			for file_name in os.listdir(new_path):
				file_path = os.path.join(new_path, file_name)
				if file_name.endswith(".txt"):
					
					if file_name == "AI_Response.txt":
						counter_AI += 1
						binary_content = read_file_as_binary(file_path)
						new_file_name_AI = "AI" + str(counter_AI) + ".txt"
						new_file_path = os.path.join(AI_train_path, new_file_name_AI)
						write_binary_to_file(binary_content, new_file_path)
					
"""
					if file_name == "solutions.json":
						with open(file_path, "r") as content:
							counter_AI += 1
							content = content.read()

							new_file_name_AI = "AI" + str(counter_AI) + ".txt"
						
							new_file_path = os.path.join(human_test_path, new_file_name_AI)
							with open(new_file_path, "w") as file:
								file.write(content)
"""

