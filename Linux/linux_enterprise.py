import requests 
import bs4
import os 



requisicao = requests.get('https://attack.mitre.org/matrices/enterprise/linux/')

bs = bs4.BeautifulSoup(requisicao.content, 'html.parser')

tatic_name = bs.find_all('td', {'class': 'tactic name'})
href_tatic = []

print(tatic_name)


# for c in tatic_name.href:
#     print(c)


number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
tatic_names = ['Initial Access', 'Execution', 'Persistence', 'Privilege Escalation', 'Defense Evasion', 'Credential Access','Discovery', 'Lateral Movement', 'Collection', 'Command and Control', 'Exfiltration', 'Impact']





