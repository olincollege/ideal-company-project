## Import the scraped dataframe from 'wikipedia_scrape.py'
from wikipedia_scrape import fortune_table

## Create the empty dictionary and list for future link containment
dict_company_links = {}
list_company_links = []

## Put all the rows of the table into a variable
## to get all the company links
fortune_rows = fortune_table.find_all('tr')

## Check through all the rows and get all the companny links
## and store them in a dictionary and library
for company_row in fortune_rows:
    row_elements = company_row.find_all("td") # Check for all the elements in the table with a 'td' tage
    # If elements in a row are not empty, then parse the data
    if row_elements != []:
        company = row_elements[0].text.strip()
        # If found a link within the table, store it and append it to the list and dictionary
        if row_elements[0].find("a"):
            company_link = "https://en.wikipedia.org"+row_elements[0].find("a")["href"] 
            dict_company_links[company] = company_link
            list_company_links.append(company_link)

## Print the dictionary and list for testing purposes
print(dict_company_links)
#print(list_company_links)



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
