import os
import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# login information
email_address = os.environ.get("email", "Couldn't find email")
username = os.environ.get("username", "Couldn't find username")
password = os.environ.get("password", "Couldn't fin password")

# Beautiful soup part
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")

soup = BeautifulSoup(response.text, 'html.parser')

listings = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

listings_links = [listing.find(name="a").get("href") for listing in listings]
listings_prices = [listing.find(class_="PropertyCardWrapper__StyledPriceLine").getText().split("+")[0].split("/")[0] for listing in listings]
listings_addresses = [listing.find(name="address").getText().strip().replace("|", "") for listing in listings]
print(listings_links)
print(listings_prices)
print(listings_addresses)

# Selenium part
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSe7cNBXDrVl8y_hiFeNTauu3fgXzb_GlNgeWf_F6Zovm-j2JQ/viewform?usp=sf_link")
driver.maximize_window()

time.sleep(6)
email_field = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_field.send_keys(email_address)
email_field.send_keys(Keys.ENTER)

time.sleep(10)
username_field = driver.find_element(By.XPATH, '//*[@id="input28"]')
username_field.send_keys(username)

password_field = driver.find_element(By.XPATH, '//*[@id="input36"]')
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)

time.sleep(15)
continue_button = driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
continue_button.click()

for n in range(len(listings)):
    time.sleep(6)
    address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_field.send_keys(listings_addresses[n])

    price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.send_keys(listings_prices[n])

    link_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field.send_keys(listings_links[n])

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

    time.sleep(4)
    new_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    new_response.click()

driver.get("https://docs.google.com/forms/d/1ZJFllDnt4a7gcDFrsLSCEee61nCir7HvM6S-b5PAoaQ/edit#responses")


# Click on link to Sheets
time.sleep(8)
link_to_sheets = driver.find_element(By.XPATH, '//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/span/span[2]')
link_to_sheets.click()

# Click on create
time.sleep(10)
create = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[15]/div/div[2]/div[3]/div[2]/span/span')
create.click()


