from selenium import webdriver
import os
import time
from time import sleep
import sys
from selenium.webdriver.common.keys import Keys


class InstagramBot:

    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('chromedriver')
        self.base_url = 'https://www.instagram.com'

        self.driver.get('{}/accounts/login/'.format(self.base_url))
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(self.username)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(self.password)
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

    def nav_user(self, user):

        self.driver.get('{}/{}/'.format(self.base_url, user))
        sleep(2)

    def see_followers(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        sleep(6)

    def actively_follow(self):
        follow = self.driver.find_elements_by_class_name('sqdOP')
        for x in follow[:11]:
            x.click()
            sleep(9)
    

if __name__ == '__main__':
    ig_bot = InstagramBot ('YOUR USERNAME', 'YOUR PASSWORD')
    ig_bot.nav_user('ACCOUNT USERNAME') 
    ig_bot.see_followers()
    ig_bot.actively_follow()
