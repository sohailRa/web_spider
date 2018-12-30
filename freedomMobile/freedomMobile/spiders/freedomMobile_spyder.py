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
        datt = response.xpath('//div[@class="phone"]')

        titles = []
        prices = []
        images = []

        for dat in datt:
            title = dat.css(".phone__title::text").extract()
            price = dat.css(".phone__copy ::text").extract()
            avoid = set(['', 'MyTab Boost']) 
            price = [x.strip() for x in price if x.strip() not in avoid]
            price = [x + " " + y for x,y in zip(price[0::2], price[1::2])]
            image = dat.css(".phone__image").css('img::attr(src)').extract()
            # image = response.css('img::attr(src)').extract()
            titles.append(title)
            prices.append(price)
            images.append(image)


        for item in zip(titles, prices, images):
            scraped_info = {
                'title' : item[0],
                'price' : item[1],
                'image_urls' : [str(item[2])]
            }
            yield scraped_info





        # def parse(self, response):
        # #Extract product information
        # dat = response.xpath('//div[@class="phone"]')
        # titles = dat.css(".phone__title::text").extract()
        # prices = dat.css(".phone__copy ::text").extract()
        # avoid = set(['', 'MyTab Boost']) 
        # prices = [x.strip() for x in prices if x.strip() not in avoid]
        # prices = [x + " " + y for x,y in zip(prices[0::2], prices[1::2])]
        # # images = dat.css(".phone__image").css('img::attr(src)').extract()
        # images = response.css('img::attr(src)').extract()


        # for item in zip(titles, prices, images):
        #     scraped_info = {
        #         'title' : item[0],
        #         'price' : item[1],
        #         'image_urls' : [item[2]]
        #     }

        #     yield scraped_info