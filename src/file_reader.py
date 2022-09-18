def file_reader(path):
    with open(path, "r") as file:
        fileLines = file.readlines() 
        return fileLines