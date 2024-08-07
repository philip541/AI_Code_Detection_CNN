import os

def read_file_as_binary(file_path):
    with open(file_path, 'rb') as file:
        binary_content = file.read()
    return binary_content

def write_binary_to_file(binary_content, output_file_path):
    with open(output_file_path, 'w') as file:
        for byte in binary_content:
            file.write(f'{byte:08b} ')
    
    print(f'Binary content has been written to {output_file_path}')

"""
directory_AI = "/Users/philipnegrin/Downloads/AICodeDetection/Titanic_Data_AI"
for file in os.listdir(directory_AI):
	path = "/Users/philipnegrin/Downloads/AICodeDetection/Titanic_Data_AI" + "/" + str(file)
	content = read_file_as_binary(path)

	file_name = str(file)[:-3] + ".txt"
	new_path = "/Users/philipnegrin/Downloads/AICodeDetection/Binary_AI"

	with open(os.path.join(new_path, file_name), 'w') as fp:
		pass

	new_file_path = new_path + "/" + file_name
	write_binary_to_file(content, new_file_path)

	

directory_Human = "/Users/philipnegrin/Downloads/AICodeDetection/Titanic_Data_Human"
for file in os.listdir(directory_Human):
	path = "/Users/philipnegrin/Downloads/AICodeDetection/Titanic_Data_Human" + "/" + str(file)
	content = read_file_as_binary(path)

	file_name = str(file)[:-6] + ".txt"
	new_path = "/Users/philipnegrin/Downloads/AICodeDetection/Binary_Human"

	with open(os.path.join(new_path, file_name), 'w') as fp:
		pass

	new_file_path = new_path + "/" + file_name
	write_binary_to_file(content, new_file_path)


	#Create a new file to write the binary content onto using OS
		#Create new folder with all the binary files


	#write_binary_to_file(content, )


#Figure out what image format sklearn cnn takes in
	#Try and find one that takes numpy arrays

"""