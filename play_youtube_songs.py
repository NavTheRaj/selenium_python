from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

song = input("Which song would you like to hear?\n")
url = "https://gaana.com/"
opts = Options()
opts.headless = True
browser = Firefox(options=opts)
browser.get(url)

search_form = browser.find_element_by_id('sb')

search_form.send_keys(song)

search_form.submit()

results = browser.find_element_by_class_name('img')

print(search_form[0].title)
