import main as main
main.init("name_and_age.csv", folder=False, dir_name="my_csv's")
print(main.read_csv())
main.write_csv({"name": ["superuser5698"], "age": ["?"]})
print(main.read_csv())