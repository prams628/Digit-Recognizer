import os

def clear(file_path):
    for file in os.listdir(file_path):
        os.remove(file_path + "\\" + file)