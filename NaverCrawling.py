import requests
import bs4

page_n = 1
page_url = f"https://finance.naver.com/sise/sise_index_time.naver?code=KPI200&thistime=20230113185900&page={page_n}"

soure = requests.get(page_url).text



# print(bs4.BeautifulSoup(soure.find('td', class_='')))

# print(soure.find_all('td'))

# print(soure.find_all('td', class_ = 'number_1'))

# print(requests.get(page_url))

# print(page_url)
