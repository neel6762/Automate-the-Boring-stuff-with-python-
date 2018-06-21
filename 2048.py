from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def openTheBrowser(url):
    browser = webdriver.Chrome(r'C:\Users\ONEST\AppData\Local\Programs\Python\Python36-32\selenium\webdriver\chromedriver_win32\chromedriver.exe')
    browser.get(url)
    target = browser.find_element_by_tag_name('body')
    while True:
        # time.sleep(1)
        if browser.find_element_by_css_selector('body > div > div.game-container > div.game-message > p').text == 'Game over!':
            break
        target.send_keys(Keys.RIGHT)

        if browser.find_element_by_css_selector('body > div > div.game-container > div.game-message > p').text == 'Game over!':
            break
        target.send_keys(Keys.DOWN)

        if browser.find_element_by_css_selector('body > div > div.game-container > div.game-message > p').text == 'Game over!':
            break
        target.send_keys(Keys.UP)

        if browser.find_element_by_css_selector('body > div > div.game-container > div.game-message > p').text == 'Game over!':
            break
        target.send_keys(Keys.LEFT)

    time.sleep(3)
    print('Game Over!')
    browser.quit()


if __name__ == '__main__':
    url = 'http://gabrielecirulli.github.io/2048/'
    openTheBrowser(url)
