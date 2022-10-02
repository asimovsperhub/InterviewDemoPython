from datetime import datetime

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == '__main__':
    setting_ = get_project_settings()
    today = datetime.now()
    setting_["csv_filename"] = "fashionnova.csv"
    setting_['fieldnames'] = ['symbol', 'name', 'current', 'percent', 'market_capital', 'pe_ttm']
    setting_["ITEM_PIPELINES"] = {
        'jysw.pipelines.CsvPipeline': 300,
    }
    # setting_["CONCURRENT_REQUESTS"] = 2
    # setting_["LOG_FILE"] = "xueqiu_{}_{}_{}.log".format(today.year, today.month, today.day)
    process = CrawlerProcess(settings=setting_)
    process.crawl("fashionnova")
    process.start()