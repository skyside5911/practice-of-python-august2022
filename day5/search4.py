#code to extract data from api  of multiple pages
import requests
# from bs4 import BeautifulSoup
count=0
for page in range(1,40):
    url = 'https://theleafdesk.com/wp-json/wp/v2/posts'+("?page=%s"%page)
    data = requests.get(url).json()
    for p in data:
        print(p)
        count+=1
        title=p['title']['rendered']
        content=p['content']['rendered']
        slug=p['slug']
        categoryy=p['categories']
        # y=BeautifulSoup(content, "lxml").text
        print(title)
        print()
        print()
        # print(content)
        # print()
        # print()
        # print(slug)
        # print()
        # print()
        # print(categoryy)
        # print()
        # print()
        
print(count)