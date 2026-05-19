import subprocess as terminal
from os import makedirs
global csv_lib
try:
    import pandas as csv_lib
except Exception:
    print("pandas not installed installing")
    terminal.run(["pip", "install", "pandas"])
global folder_name
def init(csv, folder=False, dir_name="csv's"):
    global dir_or_not, init_or_not, csv_file, folder_name
    dir_or_not = False
    init_or_not = 0
    if folder == True:
        folder_name = dir_name
        makedirs(folder_name, exist_ok=True)
        folder_name = folder_name
        dir_or_not = True
    csv_file_main = csv
    init_or_not = 1
dir_or_not = False
csv_file_main = "data.csv"
def read_csv(csv_file=csv_file_main):
    if dir_or_not == False:
        file = open(f"{csv_file}", "a+", -1, encoding="utf-8")
        file.close()
        try:
            csv_file = csv_lib.read_csv(f"{csv_file}")
        except:
            return "empty csv file"     
        return csv_file.head()
    if dir_or_not == True:
        file = open(f"{folder_name}/{csv_file}", "a+", -1, encoding="utf-8")
        file.close()
        try:
            csv_file = csv_lib.read_csv(f"{folder_name}/{csv_file}")
        except:
            return     
        return csv_file.head()


def write_csv(data, csv_file=csv_file_main):
    if dir_or_not == False:
        file = open(f"{csv_file}", "a+", -1, encoding="utf-8")
        file.close()
        writer = csv_lib.DataFrame(data)
        writer.to_csv(f"{csv_file}", mode="a", index=False)
    if dir_or_not == True:
        file = open(f"{folder_name}/{csv_file}", "a+", -1, encoding="utf-8")
        file.close()
        writer = csv_lib.DataFrame(data)
        writer.to_csv(f"{folder_name}/{csv_file}", mode="a", index=False)