import json

import scrapy

"""
加密js代码：

"""

class Fashionnova(scrapy.Spider):
    name = 'fashionnova'

    def __init__(self):
        pass

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'x-algolia-api-key': '0e7364c3b87d2ef8f6ab2064f0519abb',
            'x-algolia-application-id': 'XN5VEPVD4I'
        }
        url = 'https://xn5vepvd4i-2.algolianet.com/1/indexes/products/query?x-algolia-agent=Algolia%20for%20JavaScript%20(4.3.0)%3B%20Browser'
        data = {"query": "", "userToken": "anonymous-16c05763-c2d8-499a-ab75-74ccd1ff9ae1", "ruleContexts": ["all"],
                "analyticsTags": ["all", "desktop", "Returning", "China"], "clickAnalytics": 'true', "distinct": 1,
                "page": 0, "hitsPerPage": 48, "facetFilters": [], "facetingAfterDistinct": 'true',
                "attributesToRetrieve": ["handle", "image", "title"], "personalizationImpact": 0}
        yield scrapy.Request(url, body=json.dumps(data), headers=headers, callback=self.parse)

    def parse(self, response, **kwargs):
        print(response.text)
