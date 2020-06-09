from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

url = "https://bandcamp.com"
opts = Options()
opts.headless = True
browser = Firefox(options=opts)
browser.get(url)
browser.find_element_by_class_name('play-btn').click()
browser.close()
