import os
path =r"C:\Users\SL67715\PycharmProjects\pythonProject\Root\One\Data3\Sales"
os.chdir(path)

def read_files(filepath):
    with open(filepath, 'r') as file:
        next(file)
        for line in file.readlines():
                dept.append(line.split(",")[3])
        file.close()


dept = []
for file in os.listdir():
    filepath = f"{path}/{file}"

    if file.endswith(".dat"):
        read_files(filepath)

dept1=[int(x) for x in dept]
print(f"Total  quantity of fruits :{sum(dept1)}")