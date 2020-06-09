from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

email = "navrajkhanal61@gmail.com"
password = "Yamini@1999"
url = "https://keep.google.com"
opts = Options()
opts.headless = True
surfer = Firefox(options=opts)
surfer.get(url)
email_form = surfer.find_element_by_id('identifierId')
email_form.send_keys(email)
email_form.submit()
pass_form = surfer.find_element_by_label('Enter your password')
print(pass_form)
surfer.close()

