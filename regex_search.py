import re, os

path = r'C:\Files'
listFiles = os.listdir(path)
print('The files in the folder are \n', listFiles, "\n")
container = []

# iterate over the files in the "Files" folder and filter the .txt files
for txtFile in listFiles:
    match = re.compile(r'.*\.txt$')
    test = (str(txtFile))
    result = match.findall(test)
    storeR = str(result).strip('[]')
    container.append(storeR)

# print the filtered list
# print(container)

# setting the path to open the file in the "Files" folder

path = r'C:\Files'
holder = []         # A empty list that will store the path file
for files in container:
    files = str(files).strip("''")
    files = path + '\\' + files
    # print(files)
    holder.append(files)

# print(holder)

# take user input for searching
searchFiles = input('Enter the word to search ....')
print('\nSearching only in the text files...')

for files in holder:
   try:
       file = open(files, 'r')
       print('\nFile Opened:', files)
       fileRead = file.read()
       if searchFiles in fileRead:
           print('Search Successful\nWord found in the file:',files)
           break
       print('Closing File:', files)
       file.close()
   except FileNotFoundError:
       continue
