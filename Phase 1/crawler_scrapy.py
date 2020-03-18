import scrapy

class CostOfLivingSpider(scrapy.Spider):
    name = 'cost-of-living'
    allowed_domains = ['numbeo.com']
    start_urls = ['https://www.numbeo.com/cost-of-living/rankings_by_country.jsp?title=2019',
                 'https://www.numbeo.com/cost-of-living/rankings_current.jsp',
'https://www.numbeo.com/cost-of-living/prices_by_country.jsp?displayCurrency=USD&itemId=101&itemId=100&itemId=228&itemId=224&itemId=60&itemId=66&itemId=64&itemId=62&itemId=110&itemId=118&itemId=121&itemId=14&itemId=19&itemId=17&itemId=15&itemId=11&itemId=16&itemId=113&itemId=9&itemId=12&itemId=8&itemId=119&itemId=111&itemId=112&itemId=115&itemId=116&itemId=13&itemId=27&itemId=26&itemId=29&itemId=28&itemId=114&itemId=6&itemId=4&itemId=5&itemId=3&itemId=2&itemId=1&itemId=7&itemId=105&itemId=106&itemId=44&itemId=40&itemId=42&itemId=24&itemId=20&itemId=18&itemId=109&itemId=108&itemId=107&itemId=206&itemId=25&itemId=32&itemId=30&itemId=33']

	#note: https://www.numbeo.com/api/doc.jsp

    def parse(self, response):
        print("procesing: " + response.url)

        #Extract data using css selectors
        product_name = response.css('.product::text').extract()
        price_range = response.css('.value::text').extract()

        #Extract data using xpath
        ranking = response.xpath("//em[@title='Country Ranking']/text()").extract()
        country_name = response.xpath("//a[@class='store $p4pLog']/text()").extract()

        row_data = zip(product_name, price_range, ranking, country_name)

        #Making extracted data row wise
        for item in row_data:

            #create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                'page':response.url,
                'product_name' : item[0],
                'price_range' : item[1],
                'ranking' : item[2],
                'country_name' : item[3],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
