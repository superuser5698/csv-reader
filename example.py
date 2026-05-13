import main as main
main.init("data.csv")
print(main.read_csv("data.csv"))
main.write({"name": ["superuser5698"], "age": ["?"]})
print(main.read_csv("data.csv"))
