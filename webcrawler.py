from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from validate_email import validate_email
import json
import os


class webCrawler():
    def __init__(self, service, driver, URL, emailAddressList):
        self.service = service
        self.driver = driver
        self.URL = URL
        self.emailAddressList = emailAddressList
        self.pagesOpened = 0

    def firstWebpage(self): #sets url to user input
        self.URL = input("Enter the target webpage: ")

    def click_next_page(self):
        current_page = 1
        while True:
            next_page_url = f"{self.URL}?page={current_page}"
            self.driver.get(next_page_url)
            self.wait_for_page_load()  #Wait for the page to load
            self.scrapeEmailAddresses()  #Scrape email addresses from the current page
            current_page += 1
            self.pagesOpened += 1
            if self.pagesOpened >= 35:  #Stop after opening 35 pages
                break

    def scrapeEmailAddresses(self):
        html = self.driver.page_source  # sets a variable to be the webpage source
        soup = BeautifulSoup(html, "html.parser")  # uses bs4 to parse the html
        emailAddresses = soup.find_all(string=lambda text: "@" in text)  # searches the html to find strings containing "@"
        
        for emailAddress in emailAddresses:  # filters through found email addresses
            if emailAddress and validate_email(emailAddress) and emailAddress.text not in self.emailAddressList:
                # checks to see if email address is true, it is a valid email address and not already stored
                self.emailAddressList.append(emailAddress.text)  # stores email address
        
        # Check if the JSON file exists
        if os.path.exists('emailAddresses.json'):
            # Load existing email addresses from the JSON file
            with open('emailAddresses.json', 'r') as f:
                existing_email_addresses = json.load(f)
            
            # Combine the existing email addresses with the new ones, removing duplicates
            updated_email_addresses = list(set(existing_email_addresses + self.emailAddressList))
        else:
            updated_email_addresses = self.emailAddressList

        # Dump the updated email addresses into the JSON file
        with open('emailAddresses.json', 'w') as f:
            json.dump(updated_email_addresses, f, indent=4)

    def openPageList(self):
        self.click_next_page()  #calls the click_next_page function

    def wait_for_page_load(self):
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )



#Initialize the service and driver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

#Initializing empty lists
emailAddressList = []

#Initializing object and calling functions
Crawler = webCrawler(service, driver, "", emailAddressList)

#calling the functions to start the webscraper
Crawler.firstWebpage()
Crawler.openPageList()