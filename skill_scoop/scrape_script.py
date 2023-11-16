import os
import sys
#print(sys.path)
# import os
# import sys

# # Add the project root directory to the sys.path
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
# Get the absolute path of the current directory (skill_scoop)

# Get the absolute path of the virtual environment's site-packages directory
env_site_packages = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'env', 'Lib', 'site-packages')

# Add the scrapy path to sys.path
sys.path.append(env_site_packages)
job_scraper_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(job_scraper_path)

print(sys.path)
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from job_scraper.job_scraper.spiders.job_spider import JobSpider

def run_scraper():
    # Run scraping process
    process = CrawlerProcess(get_project_settings())
    process.crawl(JobSpider)
    process.start()

if __name__ == '__main__':
    run_scraper