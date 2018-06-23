# run from the command prompt and pass the name of the product you want to get the review
import requests, bs4, webbrowser, sys

# get the input from the command line, name of the product to get review and download the requested page
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]) + ' review')

# now search for the link to the top pages and open the top five pages
soup = bs4.BeautifulSoup(res.text, 'html.parser')
getElement = soup.select('.r a')
num = min(5, len(getElement))

# iterating over all the links and opening them
for i in range(num):
	webbrowser.open_new_tab('https://google.com' + getElement[i].get('href'))
