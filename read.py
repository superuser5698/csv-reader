import pandas as csv_reader

def read():
    file = open("data.csv", "r", -1, "utf-8")
    file.close()
    try:
        csv_file = csv_reader.read_csv('data.csv')
    except:
        return     
    return csv_file.head()