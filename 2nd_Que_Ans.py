import os
#path =r"C:\Users\SL67715\PycharmProjects\pythonProject\Root\One\Data1"
path =r"C:\Users\SL67715\PycharmProjects\pythonProject\Root\One\Data3\Sales"
#path =r"C:\Users\SL67715\PycharmProjects\pythonProject\Root\One\Data4"
os.chdir(path)

def read_files(filepath):
    with open(filepath, 'r') as file:
        next(file)
        for line in file.readlines():
            g = line.split(",")[1]
            if g=="Apple":
                fruits[g]=int(line.split(",")[3])
            elif g=="Orange":
                fruits["Orange"] = int(line.split(",")[3])
            elif g=="Grapes":
                fruits["Grapes"]= int(line.split(",")[3])

        file.close()
fruits={}
for file in os.listdir():
    filepath =f"{path}/{file}"

    if file.endswith(".dat"):
        read_files(filepath)
print(f"list of fruits :{fruits}")

