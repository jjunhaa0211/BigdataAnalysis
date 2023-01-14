import requests
import bs4

# page_n = 1
# page_url = f"https://finance.naver.com/sise/sise_index_time.naver?code=KPI200&thistime=20230113185900&page={page_n}"

# soure = requests.get(page_url).text
# soure = bs4.BeautifulSoup(soure)

# # print(soure)

# dates = soure.find_all("td", class_="date")
# print(dates[1].text)

# date_list = []

# for date in dates:
#     date_list.append(date.text)
    
# print(date_list)

# prices = soure.find_all("td", class_="number_1")
# prices[::4]

# print(prices)



# last_url = soure.find_all("td", class_="pgPR")[0].find_all("a")[0]["href"]
# print(last_url)

last_url = source.find_all("td", class_="pgPR")[0].find_all("a")[0]["href"]

last_page = last_url.split('&page=')[-1]

date_list = []
prices_list = []

for page_on in range(1, last_page+1):
    page_url = f"https://finance.naver.com/sise/sise_index_time.naver?code=KPI200&thistime=20230113185900&page={page_n}"
    source = requests.get(page_url).text
    source = bs4.BeautifulSoup(source)
    
    dates = source.find_all("td", class_="date")
    
    for date in dates:
        date_list.append(date.text)
        
    prices = source.find_all("td", class_-"number_1")
    
    for price in prices[::4]:
        prices_list.append(price.text)
        
print(len(date_list))
print(len(prices_list))