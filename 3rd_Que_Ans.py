import os
path =r"C:\Users\SL67715\PycharmProjects\pythonProject\Root\One\Data1"
#path =r"C:\Users\SL67715\PycharmProjects\pythonProject\Root\One\Data3\Sales"
#path =r"C:\Users\SL67715\PycharmProjects\pythonProject\Root\One\Data4"
os.chdir(path)

def read_files(filepath):
    with open(filepath, 'r') as file:
        next(file)
        for line in file.readlines():
            g = line.split(",")[3]
            if g in dept:
                dept[g] = line.split(",")[2]
            else:
                dept[g] = 1
        file.close()
dept={}
for file in os.listdir():
    filepath =f"{path}/{file}"

    if file.endswith(".dat"):
        read_files(filepath)
print(f"unique depts is :{dept.keys()}")

