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
        dat = response.xpath('//div[@class="phone"]')
        titles = dat.css(".phone__title::text").extract()
        desc = dat.css(".phone__copy ::text").extract()
        avoid = set(['', 'MyTab Boost']) 
        desc = [x.strip() for x in desc if x.strip() not in avoid]
        desc = [x + y for x,y in zip(desc[0::2], desc[1::2])]


        for item in zip(titles, desc):
            scraped_info = {
                'title' : item[0],
                'desc' : item[1]
            }

            yield scraped_info


# phone-data -> phone -> phone__heading - > phone__title
# phone-data -> phone -> phone_graphics - > phone__image -> scr


# aa= response.xpath('//div[@class="phone"]')
# for x in aa:                                                          
#     # title = aa.css(".phone__title::text").extract()
#     desc = aa.css(".phone__copy *::text").extract()
#    # print(desc)
        
#     count = 0
#     for x in desc:
#         if len(x) > 0:
#             count+= 1
#             print('-------------------------')
#             print('Count: ', count)
#             print(len(x))
#             print('-------------------------')


# (str(x), str(y), str(z)) for x,y,z in zip(a[0::3], a[1::3], a[2::3])]


 # for x in aa:                                                          
 #    ...:     # title = aa.css(".phone__title::text").extract()
 #    ...:     desc = aa.css(".phone__copy ::text").extract()
 #    ...:    # print(desc)
 #    ...:         
 #    ...:    # bb = [(x, y) for x,y in zip(desc[0::2], desc[2::2])]
 #    ...:     lst = []
 #    ...:     for b in desc:
 #    ...:        # b = b.strip()
 #    ...:         if len(b.strip()) > 0:
 #    ...:             print('-------------------------')
 #    ...:             item = str(b.strip().encode('ascii', 'ignore').decode('ascii'))
 #    ...:             lst.append(item)
 #    ...:             print(item)
 #    ...:             print('-------------------------')




# phones = response.xpath('normalize-space(//div[@class="phone"])').extract()

 # for phone in phones:
 #        title = aa.css(".phone__title::text").extract()
 #        desc = aa.css(".phone__copy ::text").extract()
 #        avoid = set(['', 'MyTab Boost']) 
 #        desc = [x.strip() for x in desc if x.strip() not in avoid]
 #        desc = [x + y for x,y in zip(desc[0::2], desc[1::2])]


# dat = response.xpath('//div[@class="phone"]')
# title = dat.css(".phone__title::text").extract()
# desc = dat.css(".phone__copy ::text").extract()
# avoid = set(['', 'MyTab Boost']) 
# desc = [x.strip() for x in desc if x.strip() not in avoid]
# desc = [x + y for x,y in zip(desc[0::2], desc[1::2])]