import shutil, os
# custom is a folder in my current working directory
for root, dir, files in os.walk('custom'):
    for file in files:
        if file.endswith('.txt') or file.endswith('.pdf'):
            print('Copying the file: ' + root + '\\' + file)
            shutil.copy(root + '\\' + file, r'F:\custom-new')