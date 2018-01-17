# -*- coding: utf-8 -*- 
import scrapy
import json
from scrapy_splash import SplashRequest
from ..items import NewSegundamanoItem 
from scrapy.spiders import CrawlSpider
class SegundamanoJsonSpider(scrapy.Spider):
    name = 'jsonspider16-01'
    allowed_domains = ['webapi.segundamano.mx', 'segundamano.mx']
    handle_httpstatus_list = [301, 302, 502, 200]
    download_delay = 0
    download_timeout = 280
    start_urls = ['https://webapi.segundamano.mx/nga/api/v1/public/klfst?lang=es&category=1000&lim=36']

    #@property
    def parse(self, response):
        data = json.loads(response.body)
        for jsonresponse in data.get('list_ads',[]):
            myItem = NewSegundamanoItem()
            #myItem['SIRET'] = data.get('Result')[0].get('Sections')[1].get('Tags')[18].get('Value')
            #key = data.get('Result')[0].get('Sections')[1].get('Tags')[18].get('Key')
            myItem['ANNONCE_LINK'] = jsonresponse.get('ad').get('share_link')
            ad_id = jsonresponse.get('ad').get('ad_id')
            link = myItem['ANNONCE_LINK'].split('/')
            myItem['ID_CLIENT'] = link[-1]
            myItem['ANNONCE_TEXT'] = jsonresponse.get('ad').get('body')
            myItem['ACHAT_LOC'] = jsonresponse.get('ad').get('category').get('label')  #change it with one or 2 later
            try:
                myItem['CATEGORIE'] = jsonresponse.get('ad').get('ad_details').get('estate_type').get('single').get('label') 
            except:
                pass
#            myItem['Maison_APT'] = #fill it with myItem['CATEGORIE']#change it with 1 or 2 later
            try:
                myItem['PIECE'] = jsonresponse.get('ad').get('ad_details').get('rooms').get('single').get('label')
            except:
                pass
            try:
                myItem['M2_TOTALE'] = jsonresponse.get('ad').get('ad_details').get('size').get('single').get('label')
            except:
                pass

            try:
                myItem['PAYS_AD'] = jsonresponse.get('ad').get('ad_details').get('size').get('single').get('code') #its M2_TOTALE without m2
            except:
                pass
            myItem['NOM'] = jsonresponse.get('ad').get('subject')
            try:
                myItem['PHOTO'] = len(jsonresponse.get('ad').get('images'))
            except:
                myItem['PHOTO'] = 0
            try:
                myItem['PRIX'] = jsonresponse.get('ad').get('list_price').get('price_value')
            except:
                pass
            try:
                myItem['ANNONCE_DATE'] = jsonresponse.get('ad').get('list_time').get('label')
            except:
                pass
            try:                
                myItem['REGION'] = jsonresponse.get('ad').get('locations')[0].get('label')
            except:
                pass

            try:
                myItem['PROVINCE'] = jsonresponse.get('ad').get('locations')[0].get('locations')[0].get('label')
            except:
                pass
            try:
                myItem['QUARTIER'] = jsonresponse.get('ad').get('locations')[0].get('locations')[0].get('locations')[0].get('label')
            except:
                pass
            try:
                myItem['SELLER_TYPE'] = jsonresponse.get('ad').get('type').get('label') #in reality this is the ACHAT_LOCATION change it later with 1 or 2
            except:
                pass
            try:
                myItem['AGENCE_NOM'] = jsonresponse.get('ad').get('user').get('account').get('name')
            except:
                pass
            try:
                myItem['ADRESSE'] = myItem['QUARTIER']+' ' +myItem['PROVINCE']+' '+myItem['REGION']
            except:
                pass
            #myItem[''] =
           # myItem[''] =
           # myItem[''] =
            #myItem[''] =
            #myItem[''] = 
            #myItem[''] =
            #myItem[''] =
            #myItem[''] =
            #myItem[''] =
	    full_url = 'https://webapi.segundamano.mx/nga/api/v1/public/klfst/'+myItem['ID_CLIENT']+'/phone?lang=es' 
            request = scrapy.Request(full_url, callback = self.detail_page)
           # request = SplashRequest(full_url, callback = self.detail_page)
            request.meta["myItem"] = myItem
            yield request
            #yield myItem
        
	    

    	   # yield myItem


        next_id = data.get('next_page',[])
        next_page = 'https://webapi.segundamano.mx/nga/api/v1/public/klfst?lang=es&category=1000&o='+str(next_id)+'&lim=36'
        if next_page:
            req = scrapy.Request(next_page)#,  callback=self.parse)
           # req = SplashRequest(next_page)
            yield req

        #if needed while all the onformations are not stored in the listing json page
            #url = 'https://carsales.mobi/mobiapi/carsales/v3/stock/details/'
            #full_url = url + myItem['ID_CLIENT']
            #request = scrapy.Request(full_url, callback = self.adv_page)
            #request.meta["myItem"] = myItem
            #yield request
            

    def detail_page(self, response):
	data = json.loads(response.body)
        myItem = response.meta['myItem']
        try:
        	myItem['AGENCE_TEL'] = data.get('phones',[])[0].get('label')
        except:
            pass
	yield myItem






#	pass
