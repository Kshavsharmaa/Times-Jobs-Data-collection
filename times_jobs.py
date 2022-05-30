import requests
from bs4 import BeautifulSoup
import pandas as pd

timesjob = {}

profile_list = []
campany_list = []
skills_list = []
exp_list = []
loc_list = []

for page in range(1,30):

    url = f'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=jobs&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=jobs&pDate=I&sequence={page}&startPage=1'
    html_code = requests.get(url).content
    soup = BeautifulSoup(html_code,'lxml')

    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs:

        profile = job.find('header', 'clearfix').get_text().strip().replace('\r\n','').replace('\n', '')

        campany = job.find('h3', class_ = 'joblist-comp-name').get_text().strip()
        skills = job.find('span', class_='srp-skills').get_text().strip().replace(' ','')

        info = job.find('ul', 'top-jd-dtl clearfix')
        exp = info.find_all('li')[0].get_text().replace('card_travel', ' ').strip()
        loc = info.find_all('li')[1].get_text().replace('location_on', ' ').strip()

        description = job.find('ul', 'list-job-dtl clearfix')
        job_des = description.find_all('li')[0].get_text().replace('Job Description:', ' ').strip().replace('  ', ' ')
            
        
        profile_list.append(profile)
        campany_list.append(campany)
        skills_list.append(skills)
        exp_list.append(exp)
        loc_list.append(loc)


timesjob["Profile"] = profile_list
timesjob["Campany"] = campany_list
timesjob["Skills"] = skills_list
timesjob["Exp"] = exp_list
timesjob["Location"] = loc_list

# print(timesjob)

df = pd.DataFrame(timesjob, columns=['Profile', 'Campany', 'Skills','Exp', 'Location'] )
# print(df)
# df.to_csv('timesjobs_data.csv')