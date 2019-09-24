

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector(".nowrap#num1")
    x = x_element.text
    z_element = browser.find_element_by_css_selector(".nowrap#num2")
    z = z_element.text
    y = str(int(x) + int(z))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла