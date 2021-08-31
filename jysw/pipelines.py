# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import os

from itemadapter import ItemAdapter


class JyswPipeline:
    def process_item(self, item, spider):
        return item


class CsvPipeline:
    def __init__(self, fieldnames:list, csv_filename="default.csv"):
        store_dir = os.path.dirname(__file__) + "/csv_data/"
        if "\\" in store_dir:
            store_dir = store_dir.replace("\\", "/")
        if not os.path.exists(store_dir):
            os.mkdir(store_dir)
        store_file = store_dir + csv_filename
        self.file = open(store_file, 'w', newline='', encoding='utf-8')
        self.fieldnames = fieldnames
        self.writer = csv.DictWriter(f=self.file, fieldnames=self.fieldnames)
        self.writer.writeheader()

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        csv_filename = settings.get("csv_filename")
        fieldnames = settings.get('fieldnames')
        return cls(fieldnames, csv_filename)

    def process_item(self, item, spider):
        self.writer.writerow({fieldname: item['%s' % fieldname] for fieldname in self.fieldnames})
        return item

    def close_spider(self, spider):
        self.file.close()
