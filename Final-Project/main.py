from selenium import webdriver
import time
import os

url = "https://www.pexels.com/"
driver_path = "D:/Programs/Chrome/chromedriver_win32/chromedriver.exe"
# cats_dogs_List = ['dog', 'cat']
cats_dogs_List = ['cat', 'dog']

def drive_initial(download_path):
	r"""
	see reference: https://www.cnblogs.com/presleyren/p/12936553.html
	:param download_path: str. only \\ not /
	:return: driver (Chrome only)
	"""

	chrome_options = webdriver.ChromeOptions()
	prefs = {'download.default_directory': download_path}
	chrome_options.add_experimental_option('prefs', prefs)
	chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
	chrome_options.add_experimental_option('useAutomationExtension', False)

	driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)

	driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
		"source": """
		    Object.defineProperty(navigator, 'webdriver', {
		      get: () => undefined
		    })
		  """
	})

	return driver

def crawler(url, driver):

	driver.get(url)
	time.sleep(5)  # wait to load

	result = driver.find_element_by_class_name('search__grid')  # 找到图片的位置grid
	photos = result.find_elements_by_class_name('photos')

	photo_url = []

	for p in photos:
		cols = p.find_elements_by_class_name('photos__column')
		for l1 in cols:
			photo_divs = l1.find_elements_by_class_name('hide-featured-badge')
			for f in photo_divs:
				articles = f.find_elements_by_tag_name('article')
				for ar in articles:
					art_link = ar.find_elements_by_tag_name('a')
					for a in art_link:
						url = a.get_property('href')  # Gets the given property of the element.
						#  排除头像
						if str(url).find('@') < 0 and str(url).find('download') < 0:
							photo_url.append(url)
	return photo_url

def download(driver, photo_url_list):

	photo_url_final_list = []

	for l1 in photo_url_list:
		print("Now, start download: " + str(l1))
		try:
			time.sleep(2)
			driver.get(l1)
			time.sleep(2)
			dn = driver.find_element_by_class_name('rd__button--download')
			"""
			rd_button = driver.find_element_by_class_name('rd__button--download')
			art_link = rd_button.find_elements_by_tag_name('a')
			photo_final_url = art_link.get_property('download href')
			driver.get(photo_final_url)
			"""
			time.sleep(1)
			dn.click()
			time.sleep(2)
			# final_url = dn.get_property('href')
			# photo_url_final_list.append(final_url)
			# print(final_url)
			# r = requests.request('get', url)
			print("\tDownload completed.")
		except:
			print("\tDownload fail.")
			pass

def main():
	for animal in cats_dogs_List:
		url_animal = url + "search/" + str(animal) + "/"
		print("The url is: " + url_animal + "\n")

		# Note that the dir only \\
		download_path = 'D:\\Lectures\\Open Source Tool\\Assignment\\FinalProject\\Dataset\\' + str(animal)

		if not os.path.exists(download_path):
			os.mkdir(download_path)

		driver = drive_initial(download_path)

		for page in range(1, 100):
			url_page = url_animal + "?page=" + str(page)
			print("\tNow page " + str(page) + " for " + str(animal) + " is loading...\n")

			photo_url = crawler(url=url_page, driver=driver)
			time.sleep(1)
			download(driver=driver, photo_url_list=photo_url)

		driver.close()

if __name__ == "__main__":
	main()

