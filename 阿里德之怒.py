# -*- coding: utf-8 -*-
import requests
from wxpy import *
import time, re
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from PIL import Image
import json
import sys



class Spider(object):
    def __init__(self):

        bot = Bot(cache_path=True)
        self.my_friend = bot.friends().search('', sex=MALE, city='郑州')[0]
        self.url = 'https://ald.xy.com/integralsec/gain'
        self.video_url = 'https://ald.xy.com/chiefly/moreVideo'
        self.bbs_url = 'https://ald.xy.com/bbspc/index'
        self.bbs_urls = 'https://ald.xy.com/bbspc/sign'
        self.integral_url = 'https://ald.xy.com/integralsec/detail'
        self.passname = ['']
        self.password = ''
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
        self.driver.get(self.url)
        
    def login_Sign(self):
       
        self.driver.maximize_window() 
        self.driver.find_element_by_id("auto-id-1544890886371").click()
       
        loginname = self.driver.find_element_by_id("phoneipt") 
        loginname.clear()
        loginname.send_keys(self.passname[0])
        time.sleep(1)
        loginpass = self.driver.find_element_by_id('loginpass')
        loginpass.clear()
        loginpass.send_keys(self.password)
        time.sleep(1)
        logins = self.driver.find_element_by_id('login')
        logins.click()
        time.sleep(1)
        soup = BeautifulSoup(self.driver.page_source,'lxml')

        for tag in soup.find_all('div',class_ = 'jf-login'):
            self.my_friend.send("当前帐号和积分是"+str(tag.get_text()))
        
        for i in soup.select("#signScore"):
            sigh_1 = i.string
            if sigh_1 == '点击签到':
                sigh_ = self.driver.find_element_by_link_text('点击签到')
                sigh_.click()
                #self.my_friend.send('正在进行每日签到...')
            else:
            #self.my_friend.send("每日签到签到成功，积分+1")
                pass

        if soup.find_all(text = '签到不足') == '签到不足':
            pass
            #self.my_friend.send('签到不足7日...')
        else:
            pass

        
        a = soup.find_all(href=re.compile("bbspc/index"))
        for links in a:
            if links.string == "前往签到":
                self.driver.get(self.bbs_url)
                self.driver.get(self.bbs_urls)
                self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[1]/div[5]/a').click()
                #self.my_friend.send('正在进行论坛签到...')
        html = BeautifulSoup(self.driver.page_source,'lxml')
        
        link  = html.find_all(text = "已签到")

        self.driver.get(self.video_url)
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div[1]/div[3]/a[2]/img').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div[2]/div[3]/a[2]/img').click()
        self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div[3]/div[3]/a[2]/img').click()
        #self.my_friend.send('视频点赞完毕！')
        self.driver.get(self.url)
        html_ = BeautifulSoup(self.driver.page_source,'lxml')
        if html_.find_all(text = '领取积分') == '领取积分':

            self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/a').click()
            self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/a').click()
            self.my_friend.send('正在领取签到积分...')
        else:
            self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[1]/div[3]/a').click()
         
            #self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div[1]/a').click()

        


        self.driver.get(self.url)
        soups = BeautifulSoup(self.driver.page_source,'lxml')
        for integral in soups.find_all('div',class_ = 'jf-login'):
            integrals_ = integral.get_text()
        _integrals_ = str(integrals_)
        self.my_friend.send('当前帐号和积分是:'+ _integrals_)

        self.driver.get(self.integral_url)
        time.sleep(1)

        js = "var q=document.documentElement.scrollTop=850"

        self.driver.execute_script(js)
        self.driver.get_screenshot_as_file('integral.png')


    def agentIP(self):

        proxy = '183.163.40.223:31773'
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy--seiver =http://'+proxy)
        browser = webdriver.Chrome(chrome_options = chrome_options,executable_path='/usr/local/bin/chromedriver')
        browser.get('http://httpbin.org/get')

    def ceshi(self):
        for i in self.passname:
            return i 

        

if __name__ == '__main__':

    spider = Spider()
    spider.login_Sign()
    #spider.agentIP()
    

                                
  
