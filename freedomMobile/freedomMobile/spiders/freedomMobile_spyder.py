# -*- coding: utf-8 -*-
import scrapy


class FreedommobileSpyderSpider(scrapy.Spider):
    name = 'freedomMobile_spyder'
    allowed_domains = ['www.freedommobile.ca/plans-and-devices/mobile-devices']
    start_urls = ['https://www.freedommobile.ca/plans-and-devices/mobile-devices/']

    #location of csv file
    custom_settings = {
       'FEED_URI' : 'output/%(time)s.json'
    }

# scrapy crawl freedomMobile_spyder -o 'freedomMobile/%(time)s.json'
    def parse(self, response):
        #Extract product information
        dat = response.xpath('//div[@class="phone"]')
        titles = dat.css(".phone__title::text").extract()
        desc = dat.css(".phone__copy ::text").extract()
        avoid = set(['', 'MyTab Boost']) 
        desc = [x.strip() for x in desc if x.strip() not in avoid]
        desc = [x + " " + y for x,y in zip(desc[0::2], desc[1::2])]


        for item in zip(titles, desc):
            scraped_info = {
                'title' : item[0],
                'price' : item[1]
            }

            yield scraped_info

