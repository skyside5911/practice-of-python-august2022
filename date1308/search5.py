#code to extract data from api  of multiple pages
from unicodedata import category
import requests
# from bs4 import BeautifulSoup
count=0
for page in range(1,39):
    url = 'https://theleafdesk.com/wp-json/wp/v2/posts/{}?_embed?page=%s'%page
    data = requests.get(url).json()
    for p in data:
    
        title=p['title']['rendered']
        date=p['date']
        image=p['_embedded']['wp:featuredmedia'][0]['source_url']
        featured_media=p['featured_media']
        print(title)
    # image=p['yoast_head_json']['og_image']
    # content=p['content']['rendered']
    # slug=p['slug']
    # categoryy=p['categories']
    
    # if count==2:
    #     break
    # count+=1
    # y=BeautifulSoup(content, "lxml").text
    
    # print()
    # print()
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