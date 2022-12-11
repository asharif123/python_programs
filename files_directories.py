##files/directories

from pathlib import Path
##absolute (starts from C path on windows or /usr/loca/ on macbook) 
# relative path

# path = Path("ecommerce")
# ##create directory called ecommerce
# print(path.mkdir())
# print(path.exists())
# ##remove directory
# print(path.rmdir())

##iterate spreadsheets in directory, open them and process
#change path to current dir
##use glob directory  to search for directories in current path
path = Path()
#get all the files
#*.xls searches for all excel files
for file in path.glob('*.xls'):
    print(file)
print(path.glob('*.*'))