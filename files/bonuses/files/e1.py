import glob

myfiles = glob.glob("files2\\*.txt")

for filepath in myfiles:
    with open(filepath, "r") as file:
        print(file.read())