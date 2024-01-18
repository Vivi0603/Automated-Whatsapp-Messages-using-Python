from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

# Load the Chrome driver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

# Open WhatsApp URL in Chrome browser
driver.get("https://web.whatsapp.com/")

# Read data from Excel
excel_data = pd.read_excel('Customer bulk email data.xlsx', sheet_name='Customers')

# Locate search box once
search_box_xpath = '//*[@id="side"]/div[1]/div/label/div/div[2]'
person_title = wait.until(lambda driver: driver.find_element_by_xpath(search_box_xpath))

# Iterate over each row in the dataframe
for index, row in excel_data.iterrows():
    try:
        # Prepare the message
        message = row['Message'].replace('{customer_name}', row['Name'])

        # Clear the search box and search for the contact
        person_title.clear()
        person_title.send_keys(str(row['Contact']))
        person_title.send_keys(Keys.ENTER)

        # Wait for the contact to load and send the message
        WebDriverWait(driver, 10).until(lambda d: d.find_element_by_xpath("//div[@contenteditable='true']"))
        actions = ActionChains(driver)
        actions.send_keys(message)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    except NoSuchElementException:
        # Handle case when contact is not found or message box is not available
        print(f"Contact {row['Contact']} not found or message box not available.")

# Close Chrome browser
driver.quit()
