import os
import re

path =r"C:\Users\SL67715\PycharmProjects\pythonProject\Root\One\Data3"
os.chdir(path)

def read_files(filepath):
    with open(filepath, 'r') as file:
        next(file)
        for line in file.readlines():
            a=line.split(",")[4][0:4]
            sal.append(a)
        file.close()
sal=[]
for file in os.listdir():
    filepath =f"{path}/{file}"

    if file.endswith(".dat"):
        read_files(filepath)

salary=[int(x) for x in sal]
print(f"Total  quantity of fruits :{sum(salary)}")

