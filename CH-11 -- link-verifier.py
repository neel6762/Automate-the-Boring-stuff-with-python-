import requests
import bs4
import time


def main():
    url = 'http://example.webscraping.com/'
    res = requests.get(url)
    try:
        res.raise_for_status()
    except Exception as exc:
        print('There was an exception', exc)

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    for target in soup.findAll('a'):
        time.sleep(3)
        hrefElm = target.get('href')
        print('Fetching details from the link: ' + url + hrefElm)
        try:
            res = requests.get(url + hrefElm)
            print('Successfully Fetched !')
        except Exception as exc:
            print('An Exception was cauesd: ' + exc)


if __name__ == '__main__':
    main()
