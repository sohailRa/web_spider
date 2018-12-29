# -*- coding: utf-8 -*-
import scrapy


class FreedommobileSpyderSpider(scrapy.Spider):
    name = 'freedomMobile_spyder'
    allowed_domains = ['www.freedommobile.ca/plans-and-devices/mobile-devices']
    start_urls = ['https://www.freedommobile.ca/plans-and-devices/mobile-devices/']

    #location of csv file
    custom_settings = {
       'FEED_URI' : 'freedomMobile.csv'
    }


    def parse(self, response):
        #Extract product information
        titles = response.css(".phone__title::text").extract()
        images = response.css('img::attr(src)').extract()
        price_desc = [""]


        for item in zip(titles, images, price_desc):
            scraped_info = {
                'title' : item[0],
                'image_urls' : [item[1]], #Set's the url for scrapy to download images
                'price_desc' : item[2]
            }

            yield scraped_info


