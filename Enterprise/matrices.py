import requests
import bs4
import os
import csv


def Linux():
    req = requests.get('https://attack.mitre.org/matrices/enterprise/linux/')



    bs = bs4.BeautifulSoup(req.content, 'html.parser')

    table = bs.find('table', {'class': 'matrix flat'})

    tactics_name = table.find_all('td', {'class': 'tactic name'})

    names = []
    count = []

    for c in tactics_name:
        names.append(c.text)


    tech_count = table.find_all('td', {'class': 'tactic count'})

    for c in tech_count:
        count.append(c.text.replace(u'\xa0', u' ').replace('\n', '').strip())

    dict_names = {}

    for k, v in enumerate(names):
        dict_names[names[k]] = count[k]



    os.chdir(f'{os.getcwd()}\\Enterprise')

    current = os.getcwd() + '\\Matrices'



    with open(f'{current}\\Linux.csv', 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(dict_names.keys())
        csv_writer.writerow(dict_names.values())
