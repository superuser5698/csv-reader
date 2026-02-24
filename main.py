try:  
    import pandas as csv_reader #type: ignore
except ImportError:
    print("pandas not installed installing...")
    result =  subprocess.run(["pip", "install", "pandas"])
   # print(result)
def write(data):
    import pandas as write_csv
    writer = write_csv.DataFrame(data)
    writer.to_csv('data.csv', mode="a", index=False)
import pandas as csv_reader

def read():
    file = open("data.csv", "r", -1, "utf-8")
    file.close()
    try:
        csv_file = csv_reader.read_csv('data.csv')
    except:
        return     
    return csv_file.head()

print("welcome to online job tracker :")
import subprocess
with open("data.csv",mode="a" ) as f:
    print("checked that database exsisted")
    f.close()



personnum = 0
while True:
        
        option = input("read or write, q to quit: ")
 #       print(option)
        if option == "read":
            print(read())
        elif option == "write":
            write_stuff_name = input("who's name would you like to add to comapny list: ")
            write_stuff_jobs = input(f"{write_stuff_name}'s job: ")
            semifianl_stuff = write_stuff_name + "'s job is " + write_stuff_jobs
            computer_langouage_write_stuff = {personnum: [semifianl_stuff]}
            write(computer_langouage_write_stuff)
            personnum = personnum + 1
        elif option =="q":
            break
        else:
            print("I don't understand deal with it I'm a job tracker")
