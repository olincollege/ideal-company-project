from bs4 import BeautifulSoup
import requests
import pandas as pd

wiki_url = "https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"
table_name = "wikitable sortable"

response = requests.get(wiki_url).text
soup = BeautifulSoup(response, 'lxml')

fortune_table = soup.find('table', {'class':table_name})
rows = fortune_table.find_all('tr')

dict_company_links = {}
list_company_links = []

for tr in rows:
    elements = tr.find_all("td")
    if elements != []:
        company = elements[0].text.strip()
        if elements[0].find("a"):
            link = "https://en.wikipedia.org/wiki/"+elements[0].find("a")["href"] 
            dict_company_links[company] = link
            list_company_links.append(link)

print(dict_company_links)
print(list_company_links)
















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
