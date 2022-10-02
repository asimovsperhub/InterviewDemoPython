import scrapy



class Aliexpress(scrapy.Spider):
    name = 'aliexpress'

    def __init__(self):
        pass

    def start_requests(self):
        key = 'hat'
        url = 'https://www.aliexpress.com/wholesale?catId=0&initiative_id=SB_20210831014034&SearchText=%s' % key
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        # print(response.text)
        req = response.xpath('//*[@class="JIIxO"]')
        print(req)
        # for hat in req:
        #     print(hat)
