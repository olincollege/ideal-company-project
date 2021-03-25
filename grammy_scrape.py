from bs4 import BeautifulSoup
import requests
import pandas as pd

wiki_url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Song_of_the_Year"
table_name = "wikitable sortable"

response = requests.get(wiki_url, auth=('user', 'pass'))
soup = BeautifulSoup(response.text, 'html.parser')

grammy_table = soup.find('table', {'class':table_name})
data = pd.read_html(str(grammy_table))
df = data[0]

# print(df["Winner(s)"][20]) for testing