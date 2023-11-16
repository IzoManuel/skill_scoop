from scrapy.exporters import JsonItemExporter

class CustomPipeline:
    def __init__(self):
        self.exporter = JsonItemExporter(open('scraped_data.json', 'wb'))
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()