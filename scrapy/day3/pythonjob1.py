from gettext import find
import requests
import pandas as pd
from bs4 import BeautifulSoup
# print("type a skill you want do in your job")
# familier_job=input("enter the skill ")
# print(f'finding {familier_job} skill for you ')
url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='
html_text=requests.get(url).text
soup=BeautifulSoup(html_text,'lxml')
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')  
for job in jobs:
    company_name=job.find('h3',class_='joblist-comp-name')
    skills=job.find('span',class_='srp-skills')
    more_info=job.a['href']
    time=job.find('span',class_='sim-posted')
    # if familier_job in skills:
    print(f'Company Name :- {company_name.text.lstrip()}')
    print(f'Skills Required :- {skills.text.lstrip()}')
    print(f'More_info :- {more_info}')
    print(f'Time of post :- {time.text.lstrip()} ')

    print('')
    print('')
