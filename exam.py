from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o = ChromeOptions()
o.add_experimental_option(name="detach", value=True)
driver = Chrome(options=o)
driver.maximize_window()
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Open amazon and print all category
'''driver.get("https://www.amazon.in/")
sleep(4)
a = driver.find_elements("class name", "nav-sprite")
for item in a:
    print(item.text)'''

#print top 10 movies from IMDB
'''driver.get("https://www.imdb.com/chart/top/")
sleep(4)
a = driver.find_elements("xpath", "//h3[contains(@class,'ipc-title__text')]")
for i in range(1, 11):
    print(i, a[i].text)'''

#print count of all images on amazon
'''driver.get("https://www.amazon.in/")
sleep(4)
a=driver.find_elements("tag name", "img")
print(len(a))'''

#question-4
'''driver.get("https://demoqa.com/select-menu")
driver.find_element(By.ID, "withOptGroup").click()
sleep(2)
driver.find_element(By.XPATH, "//div[text()='Group 1, option 1']").click()'''

#question-5
'''driver.get("https://www.amazon.in/")
sleep(4)
links = driver.find_elements(By.TAG_NAME,"a")
for link in links:
    print(link.get_attribute("href"))'''

#question-6
'''driver.get("https://www.amazon.in/")
sleep(4)
driver.find_element("id", "twotabsearchtextbox").send_keys("samsung")
sleep(3)
a = driver.find_elements("xpath", "//div[@class='s-suggestion-container']")
for i in a:
    print(i.text)'''

#question-7
'''driver.get("https://www.amazon.in/")
sleep(4)
a = driver.find_element("id", "nav-link-accountList")
o = ActionChains(driver)
o.move_to_element(a).perform()
sleep(2)
driver.find_element(By.LINK_TEXT, "Your Wish List").click()'''

#question-8
'''driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe")
driver.switch_to.frame("iframeResult")
driver.switch_to.frame(0)
a = driver.find_element(By.TAG_NAME, "h1").text
print(a)'''

#question-9
'''driver.get("https://www.amazon.in/")
sleep(5)
a = driver.find_element("id", "twotabsearchtextbox")
a.send_keys("Laptop")
a.send_keys(Keys.ENTER)
sleep(3)
a = driver.find_elements("xpath", "//h2//span")
for i in a:
    print(i.text)'''
