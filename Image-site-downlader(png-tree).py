import requests, bs4, random

# ask user for the photo category
imgType = input('Category:')

# url to the png site
url = 'http://pngtree.com/do/'

# get the response from the site
res = requests.get(url + imgType)
try:
    res.raise_for_status()
except Exception as exc:
    print('Sorry an error occurred:', exc)

# print(res.text)
# creating a soup object and targetting the element
soup = bs4.BeautifulSoup(res.text, 'html.parser')
element = soup.select('.pic-box a')
num = min(15, len(element))
for i in range(num):
    add = element[i].get('href')
    res = requests.get('http://pngtree.com' + add)
    soupTwo = bs4.BeautifulSoup(res.text, 'html.parser')
    elementTwo = soupTwo.select('.dbl-picbox img')
    target = elementTwo[0].get('data-original')
    res = requests.get(target)
    for chunks in res.iter_content(1000000):
        name = random.randrange(1,1000)
        file = open(imgType + str(name) + '.jpg', 'wb')
        file.write(chunks)
        file.close()

print('done')


