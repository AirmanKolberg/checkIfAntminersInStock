from time import sleep
import pyautogui
from secrets import *
from robot_variables import *
from selenium import webdriver
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

    firefox.find_element_by_id('identifierId').send_keys(gmail_account)
    pyautogui.click(x=866, y=655)
    sleep(5)

    firefox.find_element_by_id('username').send_keys(username)
    firefox.find_element_by_id('password').send_keys(gmail_password)
    pyautogui.click(x=639, y=507)
    sleep(8)

    pyautogui.click(x=84, y=201)
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
