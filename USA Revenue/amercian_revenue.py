from bs4 import BeautifulSoup
import requests
import pandas as pd
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, 'USA_Revenue.csv')


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

table = soup.find_all('table')[0]

head = [i.text.strip('\n') for i in table.find_all('th')]

body = []
# data.text for data in table.find_all('tr')[1:]
for row in table.find('tbody').find_all('tr')[1:]:
    row_data = [cell.text.strip() for cell in row.find_all('td')]
    body.append(row_data)
    # print(row_data)

df = pd.DataFrame(body, columns=head)

df.to_csv(output_path, index=False)
