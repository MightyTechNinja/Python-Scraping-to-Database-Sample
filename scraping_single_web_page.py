import requests
import MySQLdb
from bs4 import BeautifulSoup

#SQL connection data to connect and save the data in
HOST = "localhost"
USERNAME = "scraping_sample_user"
PASSWORD = ""
DATABASE = "scraping_sample_user"

#URL to be scraped
url_to_scrape = 'https://howpcrules.com/sample-page-for-web-scraping/'
#Load html's plain data into a variable
plain_html_text = requests.get(url_to_scrape)
#parse the data
soup = BeautifulSoup(plain_html_text.text, "html.parser")

#print the whole html data to screen
#print(soup.prettify())

#Get the name of the class
name_of_class = soup.h3.text.strip()

#Get all data associated with this class
basic_data_table = soup.find("table", {"summary": "Basic data for the event"});
#Get all cells in the base data table
basic_data_cells = basic_data_table.findAll('td')

#get all the different data from the table's tds
type_of_course = basic_data_cells[0].text.strip()
lecturer = basic_data_cells[1].text.strip()
number = basic_data_cells[2].text.strip()
short_text = basic_data_cells[3].text.strip()
choice_term = basic_data_cells[4].text.strip()
hours_per_week_in_term = basic_data_cells[5].text.strip()
expected_num_of_participants = basic_data_cells[6].text.strip()
maximum_participants = basic_data_cells[7].text.strip()
assignment = basic_data_cells[8].text.strip()
lecture_id = basic_data_cells[9].text.strip()
credit_points = basic_data_cells[10].text.strip()
hyperlink = basic_data_cells[11].text.strip()
language = basic_data_cells[12].text.strip()
