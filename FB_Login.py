from selenium import webdriver
from time import sleep

def login():

    #attempt login part
    usr = input('Enter Email Id:')
    pwd = input('Enter Password:')

    driver = webdriver.Chrome("F:\Scrapper\chromedriver.exe")
    driver.get('https://www.facebook.com/')
    sleep(1)

    username_box = driver.find_element_by_id('email')
    username_box.send_keys(usr)
    sleep(1)

    password_box = driver.find_element_by_id('pass')
    password_box.send_keys(pwd)

    login_box = driver.find_element_by_id('loginbutton')
    login_box.click()

    #attempting login
    print("Attempting Login.")
    #checking for the welcome string in url
    current_url = driver.current_url
    print(current_url)

    input('Press anything to quit')
    driver.quit()
    print("Finished")


login()
