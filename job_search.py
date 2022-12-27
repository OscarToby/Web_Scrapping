from bs4 import BeautifulSoup
import requests

python_jobs_text = requests.get("https://www.seek.com.au/python-jobs/in-Sydney-Olympic-Park-NSW-2127").text
soup = BeautifulSoup(python_jobs_text, 'lxml')
jobs = soup.find_all('article', class_ = 'yvsb870 yvsb871 h3f08h1 _14uh9946i _14uh9947i _14uh9949m _14uh9948m _14uh9945a h3f08h5')
for job in jobs:
    job_title = job.find('h3', class_ = 'yvsb870 _14uh9944u _1cshjhy0 _1cshjhyl _1d0g9qk4 _1cshjhys _1cshjhy21').text
    company = job.find('span', class_ = 'yvsb870 _14uh9944u _1cshjhy0 _1cshjhy2 _1cshjhy21 _1d0g9qk4 _1cshjhyd').text[3:]      
    location = job.find('a', tabindex = '-1').text
    salary = job.find('div', class_ = 'yvsb870 v28kuf0 v28kuf4 v28kuf2')
    if salary is not None:
        salary = salary.text
    description1 = job.find('ul', class_ = 'yvsb870 yvsb873 v8nw070 v8nw074').text
    description2 = job.find('span', class_ = 'yvsb870 _14uh9944u _1cshjhy0 _1cshjhy1 _1cshjhy22 _1d0g9qk4 _1cshjhy7').text
    weblink = job.div.a
    print(f'''
    Job Title:      {job_title}
    Company:        {company}
    Location:       {location}
    Salary:         {salary}
    Description:    {description1}
                    {description2}
    Weblink:        {weblink}''')