import requests 
import bs4
import os 
import re
import csv


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

for zip in zipped:
    print(zip)

print('-=' * 20)
# choice = int(input('qual das opçoes vc quer ?'))
print('-=' * 20)


tatic_counters = bs.find_all('td', class_='tactic count')
a = []

for tatic_count in tatic_counters:
    if len(a) < len(tatic_names):
        a.append(tatic_count.text.replace(u'\xa0', u' ').replace('\n', '').strip())
    else:
        break



dicts = {}
for k,v in enumerate(tatic_names):
    dicts[v] = a[k]


current = os.getcwd() + '\\Linux'
print(current)
with open(f'{current}\\Linux_counter_tatics.csv', 'w' , newline='') as f:
    # for c in dicts:
    csv_writter = csv.writer(f)
    csv_writter.writerow(dicts.keys())

    csv_writter.writerow(dicts.values())
