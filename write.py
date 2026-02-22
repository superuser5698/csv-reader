import pandas as write_csv

def write(data):
    writer = write_csv.DataFrame(data)
    writer.to_csv('data.csv', mode="a", index=False)