from bs4 import BeautifulSoup
import requests
import os
import smtplib

EMAIL_ADDRESS = os.environ.get('Gmail_Python_WebScrapping')
EMAIL_PW = os.environ.get('Gmail_Python_PW')

URL = "https://www.seek.com.au/python-jobs/in-Sydney-Olympic-Park-NSW-2127"

python_jobs = []

def find_python_jobs():
    python_jobs_text = requests.get(URL).text
    soup = BeautifulSoup(python_jobs_text, 'lxml')
    jobs = soup.find_all('article', class_ = 'yvsb870 yvsb871 h3f08h1 _14uh9946i _14uh9947i _14uh9949m _14uh9948m _14uh9945a h3f08h5')
    for job in jobs:
        job_title = job.find('h3', class_ = 'yvsb870 _14uh9944u _1cshjhy0 _1cshjhyl _1d0g9qk4 _1cshjhys _1cshjhy21').text
        python_jobs.append(f'Job Title:\t    {job_title}\n')
        company = job.find('span', class_ = 'yvsb870 _14uh9944u _1cshjhy0 _1cshjhy2 _1cshjhy21 _1d0g9qk4 _1cshjhyd').text[3:]
        python_jobs.append(f'Company:\t{company}\n')
        location = job.find('a', tabindex = '-1').text
        python_jobs.append(f'Location:\t  {location}\n')
        salary = job.find('div', class_ = 'yvsb870 v28kuf0 v28kuf4 v28kuf2')
        if salary is not None:
            salary = salary.text
        python_jobs.append(f'Salary:\t\t   {salary}\n')
        description1 = job.find('ul', class_ = 'yvsb870 yvsb873 v8nw070 v8nw074').text
        description2 = job.find('span', class_ = 'yvsb870 _14uh9944u _1cshjhy0 _1cshjhy1 _1cshjhy22 _1d0g9qk4 _1cshjhy7').text
        python_jobs.append(f'Description:\t{description1}\n\t\t\t{description2}\n')
        node = job.h3.a['href']
        weblink = f'https://www.seek.com.au{node}'
        python_jobs.append(f'Weblink:\t{weblink}\n\n')

find_python_jobs()
python_jobs = ''.join(python_jobs)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PW)

    subject = 'Python Developer Jobs'
    body = python_jobs

    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)