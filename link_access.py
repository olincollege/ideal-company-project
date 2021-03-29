# from bs4 import BeautifulSoup
import requests
#import pandas as pd

wiki_url = "https://en.wikipedia.org/wiki/Grammy_Award_for_Song_of_the_Year"
table_name = "wikitable sortable"

response = requests.get(wiki_url, auth=('user', 'pass'))
# soup = BeautifulSoup(response.text, 'lxml')

#grammy_table = soup.find('table', {'class':table_name})
import bs4 as bs
import pandas as pd

soup = bs.BeautifulSoup(response.text, 'lxml')
parsed_table = soup.find('table', {'class':table_name})
data = [[td.a['href'] if td.find('a') else 
            ''.join(td.stripped_strings)
            for td in row.find_all('td')]
        for row in parsed_table.find_all('tr')]
df = pd.DataFrame(data[1:], columns=data[0])
print(df)
















# thead = grammy_table.find('data-colname')
# column_names = [th.text.strip() for th in thead.find_all('th')]

# table_rows = grammy_table.find_all('tr')
# link_data_by_row = []

# for row in table_rows:
#     row_data = []
#     for td in row.find_all('td'):
#         check_element = td.find('a')
#         if check_element is not None:
#             link = td.a['href']
#             row_data.append(link)
#         else: 
#             no_link = ''.join(td.stripped_strings)
#             if no_link =='':
#                 no_link = None
#             row_data.append(no_link)
#     link_data_by_row.append(row_data)

# link_dataframe = pd.DataFrame(link_data_by_row, columns = column_names)
# print(link_dataframe)



# works = pd.read_html(grammy_table, match = 'Works')
# grammy_links = grammy_table.find_all('a')


#print(grammy_links)
