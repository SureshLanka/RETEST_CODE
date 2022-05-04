import glob
path = r"C:\Users\SL67715\PycharmProjects\pythonProject\Root\One\Data1"
all_files = glob.glob(path+"/*.dat")
count = 0
for file in all_files:
    count += 1
print(f"total .dat files : {count}")