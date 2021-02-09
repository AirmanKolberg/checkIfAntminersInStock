from time import sleep
import pyautogui
from secrets import *
from robot_variables import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import system


def clear_screen():
    _ = system('clear')


def check_in_stock():
    firefox = webdriver.Firefox()
    firefox.get(bitmain_url)
    sleep(5)
    source = firefox.page_source
    firefox.close()
    clear_screen()

    if 'Sold Out' in source:
        return False
    else:
        return True


def notify_of_new_stock(subject_line, message_body):
    firefox = webdriver.Firefox()
    firefox.get(gmail_url)
    firefox.maximize_window()
    sleep(3)

    firefox.find_element_by_id('identifierId').send_keys(gmail_account)
    firefox.find_element_by_id('identifierId').send_keys(Keys.RETURN)
    sleep(5)

    firefox.find_element_by_id('username').send_keys(username)
    firefox.find_element_by_id('password').send_keys(gmail_password)
    firefox.find_element_by_id('password').send_keys(Keys.RETURN)
    sleep(5)
    firefox.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
    sleep(5)

    pyautogui.write(username)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.write(subject_line)
    pyautogui.press('enter')
    pyautogui.press('tab')
    pyautogui.write(message_body)
    firefox.find_element_by_id(':q0').click()
    firefox.close()
    clear_screen()
