import sys
#print(sys.path)
import scrapy
from urllib.parse import urljoin
print("Scraping ABOVE PIPELINE IMPORT")
from pipelines import CustomPipeline
print("Scraping BELOW PIPELINE IMPORT")
class JobSpider(scrapy.Spider):
    name = 'job_spider'
    start_urls = ['https://www.myjobmag.co.ke/jobs-by-field/information-technology']

    skills_to_search = {'python'}

    print("Scraping ABOVE CUSTOME SETTING")
    custom_settings = {
        'ITEM_PIPELINES': {'skill_scoop.pipelines.CustomPipeline': 300}
    }
    print("Scraping BELOW CUSTOME SETTING")

    def start_requests(self):
        print("Scraping START REQUEST")
        # Define number of pages to srape
        num_pages = 2
        
        for page_number in range(1, num_pages + 1):
            url = f'https://www.myjobmag.co.ke/jobs-by-field/information-technology/{page_number}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("Scraping PARSE")
        for job_listing in response.css('ul.job-list li.job-list-li'):
            yield {
                'title': job_listing.css('h2 a::text').get(),
                #'description_summary': job_listing.css('li.job-desc::text').get(),
                'job_link': job_listing.css('h2 a::attr(href)').get()
            }

            job_link = job_listing.css('h2 a::attr(href)').get()
            full_job_link = urljoin(response.url, job_link)
            yield scrapy.Request(url=full_job_link, callback=self.parse_job_page)


    def parse_job_page(self, response):
        print("Scraping PARSE_JOB_PAGE")
        # Extracting job details
        job_title = response.css('h2.mag-b span.subjob-title::text').get()
        date_posted = response.css('div.read-date-sec-li#posted-date::text').get()
        job_type = response.css('li span.jkey-info a[href*="jobs-by-type"]::text').get()
        qualification = response.css('li span.jkey-info a[href*="jobs-by-education"]::text').get()
        experience = response.css('li span.jkey-info::text').get()
        location = response.css('li span.jkey-info a[href*="jobs-location"]::text').get()
        job_field = response.css('li span.jkey-info a[href*="jobs-by-field"]::text').get()
        full_description = ' '.join(response.css('div.job-details ul li::text').getall()).strip()

        # check if any of the skills in skills_to_search are mentioned in description
        found_skills = [skill for skill in self.skills_to_search if skill.lower() in full_description.lower()]
        
        if found_skills:
            yield {
                'job_title': job_title,
                'date_posted': date_posted, 
                'job_type': job_type,
                'qualification': qualification,
                'experience': experience,
                'location': location,
                'job_field': job_field,
                'full_description': full_description,
            }

