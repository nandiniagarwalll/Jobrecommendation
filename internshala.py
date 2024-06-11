from bs4 import BeautifulSoup
import requests

def find_jobs():
    url = 'https://internshala.com/jobs/'
    response = requests.get(url)
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, 'lxml')  # Correct spelling to 'lxml'
    jobs = soup.find_all('div', class_='individual_internship')  # Correct class name spelling
    
    for job in jobs:
        name = job.find('h3', class_='job-internship-name').text.strip()  # Correct class name spelling
        more_info = 'https://internshala.com' + job['data-href']  # Add base URL to relative path

        print(f"Job Name: {name}\n")
        print(f"For more info: {more_info}\n")

if __name__ == '__main__':
    find_jobs()
