# import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# spider_path = os.path.join(os.path.dirname(BASE_DIR), 'job_scraper\job_scraper\spiders')
# import sys
# print(sys.path)
# import sys
# sys.path.append(spider_path)
from django.http import JsonResponse
import subprocess
# from job_spider import JobSpider
# from scrapy.crawler import CrawlerProcess
# from scrapy.utils.project import get_project_settings


def trigger_scraping(request):
    try:
        subprocess.run(['python', 'scrape_script.py'])
        return JsonResponse({'message': 'Scraping process triggered successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)