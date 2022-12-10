import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome

#def crawl(driver, queueList, maxDepth, curDepth):
#	if (curDepth < maxDepth):
#		url = queueList[curDepth].pop()
#		driver.get(url)
#		time.sleep(7)
#		elems = driver.find_elements(By.TAG_NAME, "a")
#		for e in elems:
#			href = e.get_attribute("href")
#			queueList[curDepth + 1].append(href)
#		if not queueList[curDepth]:
#			curDepth = curDepth + 1
#		return crawl(driver, queueList, maxDepth, curDepth)
#	else:
#		return queueList

def main():
	args = sys.argv
	if (len(args) < 2):
		print ("No command line arguments given.")
		return 1
	else:
		try:
			startURL = args[args.index("-start") + 1]
		except ValueError:
			print ("Error: Some parameters incorrect or missing.")
			return 1
	driver = webdriver.Chrome()
	driver.get(startURL)
	time.sleep(7)
	all_cookies = driver.get_cookies();
	cookies_dict = {}
	for cookie in all_cookies:
		cookies_dict[cookie['name']] = cookie['value']
	print(cookies_dict)
	# links = [[],[],[]]
	# links[0].append(startURL)
	# links = crawl(driver, links, 2, 0)
	# while (links[2]):
	#	a = links[2].pop()
	#	print(a)
	driver.close()


if __name__ == "__main__":
	main()