import requests 
import bs4
import os 
import re
import csv

def parsing_content() -> str:
    """
    This function will do the request and create the csv file with the techniques count
    
    """
    req = requests.get('https://attack.mitre.org/matrices/enterprise/linux/')

    bs = bs4.BeautifulSoup(req.content, 'html.parser')

    tatic_name = bs.find_all('td', {'class': 'tactic name'})
    href_tatic = []


    for c in tatic_name:
        href_tatic.append(c.a['href'])


    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    tatic_names = ['Initial Access', 'Execution', 'Persistence', 
                'Privilege Escalation', 'Defense Evasion', 'Credential Access',
                'Discovery', 'Lateral Movement', 'Collection',
                    'Command and Control', 'Exfiltration', 'Impact']


    zipped = zip(number, tatic_names)

    for zipp in zipped:
        print(zipp)

    print('-=' * 20)
    choice = int(input('qual das opçoes vc quer ?'))
    print('-=' * 20)


    tatic_counters = bs.find_all('td', class_='tactic count')
    tatic_counts = []

    for tatic_count in tatic_counters:
        if len(tatic_counts) < len(tatic_names):
            tatic_counts.append(tatic_count.text.replace(u'\xa0', u' ').replace('\n', '').strip())
        else:
            break


    dicts = {}
    for k,v in enumerate(tatic_names):
        dicts[v] = tatic_counts[k]


    current = os.getcwd() + '\\Linux'

    with open(f'{current}\\Linux_counter_tatics.csv', 'w' , newline='') as f:
        # for c in dicts:
        csv_writter = csv.writer(f)
        csv_writter.writerow(dicts.keys())

        csv_writter.writerow(dicts.values())

    return href_tatic[choice]


def tactics():
    req = requests.get(f'https://attack.mitre.org{parsing_content()}')
    beuaty_soup = bs4.BeautifulSoup(req.content, 'html.parser')
    Table = beuaty_soup.find('table', {'class': 'table-techniques'})
    bs = Table.find_all('td', colspan='2')
    
    headers = []
    headers.append(bs[0])
    del bs[0]
    name_id = []
      
    for c in bs:
        name_id.append(c.text.replace('\n', ''))
    print(f'The tactics are -> {name_id}')
    print('=' * 30)
    print()

    return name_id


option = int(input('qual c quer'))
