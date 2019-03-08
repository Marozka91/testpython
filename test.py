from selenium import webdriver

# Открытие браузера - open_driver
def open_driver():
    global driver
    driver = webdriver.Firefox()
    driver.get("http://www.google.com")


open_driver()
 
elem = driver.find_element_by_name("q")
elem.send_keys("Hello WebDriver!")
elem.submit()
 
print(driver.title)
