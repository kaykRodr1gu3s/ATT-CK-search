import requests 
import bs4
import os 
import re



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
choice = int(input('qual das opçoes vc quer ?'))
print('-=' * 20)


count_techniques = bs.find('div', {'class': 'matrix-container p-3'})
count_techniques = count_techniques.find_all('td', {'class' : 'tactic count'})

print(count_techniques)