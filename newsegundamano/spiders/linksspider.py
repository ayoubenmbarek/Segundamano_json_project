import scrapy
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import re , urllib ,  urllib2
from scrapy_splash import SplashRequest
from ..items import NewSegundamanoItem
from selenium import webdriver
from selenium.webdriver.common.by import By
class DmozSpider(scrapy.Spider):
        name = "linksspider1"
        allowed_domains = ["segundamano.mx"]
        start_urls = [l.strip() for l in open('/home/databiz41/newsegundamano/newsegundamano/annonce2.csv').readlines()]

	def start_requests(self):
        	for url in self.start_urls:
           		yield scrapy.Request(url, meta={
				'splash': {
				    'autoload': 'https://code.jquery.com/jquery-1.5.1.min.js',
				   # 'runjs';:
				    'endpoint': 'render.html',
				    'args': {'wait': 0.5}
				}
			    })
        def parse(self, response):
            myItem = NewSegundamanoItem()
	    #a = urllib2.urlopen('https://www.segundamano.mx/vi/916039854','').read()
	    #soup = BeautifulSoup(a)
	    #hidden_tags = soup.find_all("div", type="hidden")
	    #for tag in hidden_tags:
	#	myItem['AGENCE_TEL'] = tag.value
	    ##myItem['ANNONCE_LINK'] = response.body
	    
	   # driver = webdriver.Chrome('/home/databiz41/chrome/chromedriver')
	    #driver.get(response.url)
	    #actionChains = ActionChains(driver)
	    #click_phone = driver.find_element(By.XPATH, "//span[@class='ar-CoverPhone ar-CoverPhone_Text']")
	    #actionChains.double_click(click_phone).perform()
	 #   click_phone = driver.find_element(By.XPATH, "//span[@class='ar-CoverPhone ar-CoverPhone_Text']")
          #  click_phone.click()
	    #myItem['AGENCE_TEL'] = driver.find_element(By.XPATH, ".//label[@class='av-AdReplay_ShopDataBottom-loc']/text()")
            #myItem['AGENCE_TEL'] = response.xpath('//label[@class="av-AdReplay_ShopDataBottom-label"]/text()').extract_first() 
	    myItem['AGENCE_TEL'] = response.xpath('//*[@id="sw-Ad-reply"]/div/div/div/text()').extract_first()
	    #av-PhoneNumber
           # myItem['ANNONCE_LINK'] = response.url
	   # driver.close()
            yield myItem

