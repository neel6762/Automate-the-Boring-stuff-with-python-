import re, os

# set a location to search for
path = r'C:\Files'
files = os.listdir(path)

# to filter the text files in the folder
storeTxtFiles = []
for txtFile in files:
    if txtFile.endswith('.txt'):
        storeTxtFiles.append(txtFile)

# get the user input to search the word in the files
search = input('Enter the word to search in the text files..')
val = 0
for files in storeTxtFiles:
    match = re.compile(search)
    openedFile = open(path + '\\' + files)
    fileData = openedFile.read()
    if  match.search(fileData):
        print('Search Successful' + '\nWord found in the file:' + files)
        val = 1
        break
if val == 0:
    print('Sorry the word was not found !')
