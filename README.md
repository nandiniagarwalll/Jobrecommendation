# Jobrecommendation
This project aims to automate the process of finding and saving job listings from two popular job websites: Internshala and TimesJobs. It utilizes web scraping techniques to extract job details and store them locally for easy access. A folder named posts will be created locally on your device displaying information about different jobs available in the domain.

# Features
Internshala Job Finder: Scrapes Internshala for internship opportunities and saves relevant job details including job name and more information link.
TimesJobs Job Finder: Searches for internship listings on TimesJobs based on specified search criteria (such as computer science internships) and filters out jobs that require skills the user is unfamiliar with. Saves job details like company name, required skills, and more information link.

# SetUpInstructions
1. Clone the repository
2. Install dependencies -> BeautifulSoup and requests
3. Run the final script -> python final.py

# Usage
Upon running the script, you will be prompted to select either Internshala or TimesJobs.
Depending on your choice, the script will scrape the respective website for job listings.
For TimesJobs, you will need to input a skill you are unfamiliar with to filter out irrelevant jobs.
Job details will be saved in text files under the 'posts' directory.
