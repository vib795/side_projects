# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:40:01 2020

@author: Utkarsh Singh
"""
######################################################################
#you need selenium in your environment to run this.                  # 
#before anything open anaconda environments and install selenium and # 
#all the other dependecies anaconda shows you.                       #
#you are good to go after that with this code.                       #
######################################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()
    
    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        
    def like_insta(self, hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        #bot.find_element_by_class_name("eLAPa").click()
        bot.find_element_by_class_name("_9AhH0").click()
        time.sleep(1)
        for i in range(1, 1000):
            time.sleep(2)
            bot.find_element_by_class_name("wpO6b ").click()
            time.sleep(3)
            bot.find_element_by_class_name("coreSpriteRightPaginationArrow").click()
            t = random.randint(60,180)
            print("Will sleep for: " + str(t))
            time.sleep(t)
        bot.close()
        
ed = InstagramBot('coca_cola_t', 'cocacoal')
ed.login()
ed.like_insta('nature')