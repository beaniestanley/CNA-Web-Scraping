import urllib3
from bs4 import BeautifulSoup

url = 'https://www.channelnewsasia.com/news/singapore'

http = urllib3.PoolManager()
user_search = input("Enter:")
url = "https://www.channelnewsasia.com/action/news/8396414/search?query=" + user_search.replace(" ", "+")
response = http.request('GET', url)
soup_BS = BeautifulSoup(response.data, 'html.parser')
# print(soup_BS)

title_soup_BS = soup_BS.find_all('a', {'class': "teaser__title"})

# print(title_soup_BS)

count = 1
for title in title_soup_BS:
    if count == 10:
        break
    count += 1
    results = dict()
    results['title'] = title.text.strip()
    results['url'] = title.get('href')
    print(results)

ttp = urllib3.PoolManager()
url = 'https://www.channelnewsasia.com/news/singapore'
response = http.request('GET', url)
soup_BS = BeautifulSoup(response.data, 'html.parser')
#print(soup_BS)

ugrid_soup_BS = soup_BS.find_all('div', {'class':"u-grid"})

for t in ugrid_soup_BS:
    top_stories_BS = t.find('h2', {'class':"section__title"})
    print(top_stories_BS)

    if top_stories_BS is None:
        continue
    test = top_stories_BS.text.strip().lower()

    if 'top' in test:
        count = 1
        top = t.find_all('a', {'class': "teaser__title"})
        for title in top:
            if count == 10:
                break
            count += 1
            results = dict()
            results['title'] = title.text.strip()
            results['url'] = title.get('href')
            print(results)
