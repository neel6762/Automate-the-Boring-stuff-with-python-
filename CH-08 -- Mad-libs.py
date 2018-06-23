# doing this without the use of Regular Expression
file = open('madlibs.txt')
content = list(file.read().split())

print('The ADJECTIVE panda walked to the NOUN and then VERB')
print('\nEnter in the following words to replace them above and see the new string !')
adj = input('Adjective:')
noun = input('Noun:')
verb = input('verb:')

for i, char in enumerate(content):
    if char == 'ADJECTIVE':
        content[i] = adj
    if char == 'NOUN':
        content[i] = noun
    if char == 'VERB':
        content[i] = verb

newString = " ".join(str(x) for x in content)
print(newString)
file.close()
file = open('madlibs.txt', 'w')
file.write(newString)
file.close()
