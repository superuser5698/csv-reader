import subprocess as terminal
try:
    import pandas as csv_lib
except Exception:
    print("pandas not installed installing")
    terminal.run(["pip", "install", "pandas"])
init_or_not = 0
def init(csv):
    global csv_file, init_or_not
    csv_file = csv
    init_or_not = 1
def read_csv(csv_file):
    if init_or_not == 0:
        csv_file = "data.csv"
    file = open(csv_file, "a+", -1, encoding="utf-8")
    file.close()
    try:
        csv_file = csv_lib.read_csv(csv_file)
    except:
        return     
    return csv_file.head()
def write(data):
    global csv_file
    if init_or_not == 0:
        csv_file = "data.csv"
    file = open(csv_file, "a+", -1, encoding="utf-8")
    file.close()
    writer = csv_lib.DataFrame(data)
    writer.to_csv(csv_file, mode="a", index=False)
