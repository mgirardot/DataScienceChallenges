import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from recettes.items import RecettesItem

from scrapy.http import HtmlResponse

class RecetteSpider(Spider):
	name="recettes"
	allowed_domains = []
	urls = ["http://www.750g.com/recettes_plats.htm?page="+str(x) for x in range(2,2186)]
	start_urls = ["http://www.750g.com/recettes_plats.htm"]+ urls

	#extract recettes links
	def parse(self,response):
		hxs = Selector(response)
		for href in hxs.xpath("//body/div[@class='main-wrapper']/div[@class='main-wrapper__content']/div[@class='u-container u-container--grey']/section/div[@class='c-recipe-row__body']/h2[@class='c-recipe-row__title']/a[@class='u-link-wrapper']/@href").extract():
			if href is not None:
				child_page = response.urljoin(href)
				yield scrapy.Request(child_page, callback=self.parse_recette)
		#next_page = hxs.xpath("//body/div[@class='main-wrapper']/div[@class='main-wrapper__content']/div[@class='u-container u-container--grey u-padding-bottom']/ul[@class='c-pagination']/li[@class='c-pagination__item']/a/@href").extract_first()
		#if next_page is not None:
		#	child_page = response.urljoin(next_page)
		#	yield scrapy.Request(child_page, callback=self.parse)

	def parse_recette(self, response):
		self.log('parsing details of: %s' % response.url)
		
		try:
			hxs = Selector(response)
			#open items
			item = RecettesItem()
			#collect 
			item['nom'] = hxs.xpath("//body/div[@class='main-wrapper']/div[@class='main-wrapper__content']/div[@class='u-container']/article/header/h1/text()").extract_first()
			item['ingredients'] = hxs.xpath("//body/div[@class='main-wrapper']/div[@class='main-wrapper__content']/div[@class='u-container']/div/div/ul[@class='c-recipe-ingredients__list']/li/text()").extract()
			yield item	

		except AttributeError:
			self.log('No data to extract from : %s' % response.url)