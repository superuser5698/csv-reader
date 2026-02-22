print("welcome to online job tracker :)")
import subprocess
import read, write

try:  
    import pandas as pd #type: ignore
except ImportError:
    print("pandas not installed installing...")
    result =  subprocess.run(["pip", "install", "pandas"])
   # print(result)
def main():
    personnum = 0
    while True:
        
        option = input("read or write, q to quit: ")
 #       print(option)
        if option == "read":
            print(read.read())
        elif option == "write":
            write_stuff_name = input("who's name would you like to add to comapny list: ")
            write_stuff_jobs = input(f"{write_stuff_name}'s job: ")
            semifianl_stuff = write_stuff_name + "'s job is " + write_stuff_jobs
            computer_langouage_write_stuff = {personnum: [semifianl_stuff]}
            write.write(computer_langouage_write_stuff)
            personnum = personnum + 1
        elif option =="q":
            break
        else:
            print("I don't understand deal with it I'm a job tracker")


main()
