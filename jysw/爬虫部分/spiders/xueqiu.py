import json
import time
import scrapy

from InterviewDemoPython.jysw.爬虫部分.items import XueqiuItem


class Xueqiu(scrapy.Spider):
    name = 'xueqiu'

    def __init__(self):
        pass

    def start_requests(self):
        time_ = int(round(time.time() * 1000))
        # desc倒序 asc 正序  size 行数  时间戳：1630396522349
        url = 'https://xueqiu.com/service/v5/stock/screener/quote/list?page=1&size=100&order=desc&orderby=percent&order_by=percent&market=US&type=us&_=%d' % time_
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):
        item = XueqiuItem()
        data = json.loads(response.text)
        if data.get('data').get('list'):
            for data_ in data.get('data').get('list'):
                item['symbol'] = data_.get('symbol')
                item['name'] = data_.get('name')
                item['current'] = data_.get('current')
                item['percent'] = data_.get('percent')
                item['market_capital'] = data_.get('market_capital')
                item['pe_ttm'] = data_.get('pe_ttm')
                yield item
