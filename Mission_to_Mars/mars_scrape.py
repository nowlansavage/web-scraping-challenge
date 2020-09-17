def scrape():
	#import dependancies
	from bs4 import BeautifulSoup
	import pandas as pd
	from splinter import Browser
	import requests
	import time

	#mars news
	#url to be scraped
	url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
	#set up chromedriver
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=True)
	browser.visit(url)
	html = browser.html
	time.sleep(2)
	#scrape html
	soup = BeautifulSoup(html, 'html.parser')
	#get latest headline
	latest_headline=soup.find_all('li', class_='slide')[0].find('div', class_='content_title').text

	news_p=soup.find('div', class_='article_teaser_body').text


	#Scrape image
	url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=True)
	browser.visit(url)

	#click on featured image
	browser.click_link_by_partial_text('FULL IMAGE')
	#click on more info
	browser.click_link_by_partial_text('more info')

	#scrape html to get picture link name
	html = browser.html
	soup = BeautifulSoup(html, 'html.parser')
	#click to full image jpg link
	image_link = soup.find('aside', class_='image_detail_module').find_all('div', class_='download_tiff')[1].find('a').text
	browser.click_link_by_partial_text(image_link)
	#get the url as string
	featured_image_url = browser.url

	#scrape Mars Facts
	#set up browser
	url='https://space-facts.com/mars/'
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=True)
	browser.visit(url)
	#scapre tables using pandas
	tables =pd.read_html(browser.html)
	#get stats table into a data frame
	mars_table_df=tables[0]
	#get html for that table
	mars_table_html = mars_table_df.to_html()
	

	#crape hemispheres
	#set up browser
	url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	executable_path = {'executable_path': 'chromedriver.exe'}
	browser = Browser('chrome', **executable_path, headless=True)
	browser.visit(url)
	#create beautiful soup object for scraping
	html = browser.html
	soup = BeautifulSoup(html, 'html.parser')
	#get list of hemispheres
	hemispheres = soup.find('div', class_='collapsible results').find_all('div', class_='item')


	hemi_list=[]
	base_url='https://astrogeology.usgs.gov'

	for hemisphere in hemispheres:
	    mars_dict={}
	    link = hemisphere.find('div', class_='description').a['href']
	    title = hemisphere.find('div', class_='description').find('h3').text
	    browser.visit(base_url+link)
	    time.sleep(2)
	    html = browser.html
	    soup = BeautifulSoup(html, 'html.parser')
	    img_url = soup.find('div', class_='downloads').find('a', target='_blank')['href']
	    mars_dict['title'] = title
	    mars_dict['img_url'] = img_url
	    hemi_list.append(mars_dict)
	mars_info_dict = {
	    'featured_news_title': latest_headline, 
	    'featured_news_p': news_p, 
	    'featured_image': featured_image_url,
	    'mars_fact_table': mars_table_html,
	    'hemisphere_imgs':hemi_list
	}
	return mars_info_dict
	
	
