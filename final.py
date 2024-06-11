from bs4 import BeautifulSoup
import requests
import os
import time

def find_internshala_jobs():
    url = 'https://internshala.com/jobs/'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    jobs = soup.find_all('div', class_='individual_internship')

    posts_folder = 'posts'
    if not os.path.exists(posts_folder):
        os.makedirs(posts_folder)

    for index, job in enumerate(jobs):
        try:
            name = job.find('h3', class_='job-internship-name').text.strip()
            more_info = 'https://internshala.com' + job['data-href']

            
            with open(os.path.join(posts_folder, f'Internshala_{index}.txt'), 'w') as f:
                f.write(f"Job Name: {name}\n")
                f.write(f"For more info: {more_info}\n")

            print(f'File saved: Internshala_{index}.txt\n')
        except AttributeError:
            continue

def find_timesjobs_jobs(unfamiliar_skill):
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=internship+computer+science&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    posts_folder = 'posts'
    if not os.path.exists(posts_folder):
        os.makedirs(posts_folder)

    for index, job in enumerate(jobs):
        job_published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in job_published_date:
            company = job.find('h3', class_='joblist-comp-name').text.strip()
            skills = job.find('span', class_='srp-skills').text.replace(' ', '').strip()
            more_info = job.header.h2.a['href']
            if unfamiliar_skill.lower() not in skills.lower(): 
                with open(os.path.join(posts_folder, f'TimesJobs_{index}.txt'), 'w') as f:
                    f.write(f"Company Name: {company}\n")
                    f.write(f"Required Skills: {skills}\n")
                    f.write(f"More Info: {more_info}\n")

                print(f'File saved: TimesJobs_{index}.txt\n')

if __name__ == '__main__':
    print("Select the website you want to explore:")
    print("1. Internshala")
    print("2. TimesJobs")
    choice = input("> ")

    if choice == '1':
        find_internshala_jobs()
    elif choice == '2':
        print('Skill you are not familiar with')
        unfamiliar_skill = input('> ')
        print(f'Filtering out: {unfamiliar_skill}')

        while True:
            find_timesjobs_jobs(unfamiliar_skill)
            time_wait = 10
            print(f'Waiting {time_wait} minutes')
            time.sleep(time_wait * 60)
    else:
        print("Invalid choice. Please select 1 or 2.")


