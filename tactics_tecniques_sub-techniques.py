import requests
import re
import bs4


class listing_tactics:
    def __init__(self):
        self.link_base = 'https://attack.mitre.org'

    def getting_tactics(self) -> list:
        tactics_link = []

        req = requests.get(f'{self.link_base}/tactics/enterprise/')
        bs = bs4.BeautifulSoup(req.content, 'html.parser')
        bs = bs.find('table', class_='table table-bordered table-alternate mt-2')
        bs4_tactics = bs.find_all('a', href=re.compile(r'/tactics/TA[\d]+'))

        for link in bs4_tactics:
            
            if link['href'] not in tactics_link:

                tactics_link.append(link['href'])
            else:
                continue

        return tactics_link

    def options(self) -> int:
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9', '10', '11', '12', '13']
        name = ['Reconnaissance', 'Resource Development', 'Initial Access', 'Execution', 'Persistence', 'Privilege Escalation', 'Defense Evasion',
                'Credential Access', 'Discovery', 'Lateral Movement', 'Collection', 'Command and Control', 'Exfiltration', 'Impact']  


        conc = zip(number, name)

        print('Choice one option')
        print('=' * 30)
        for c in conc:
            print(c)

        print('=' * 30)

        choice = int(input('which of the choices: '))
        print()
        print(f'You choice the {name[choice].upper()} option')
        print()

        return choice

    def tactics(self, getting_tactic, option) -> list:
        req = requests.get(f'{self.link_base}/{getting_tactic[option]}')


        beuaty_soup = bs4.BeautifulSoup(req.content, 'html.parser')
        Table = beuaty_soup.find('table', {'class': 'table-techniques'})

        headers = []
        bs = Table.find_all('td', colspan='2')
        headers.append(bs[0])
        del bs[0]


        name_id = []
        for c in bs:
            name_id.append(c.text.replace('\n', ''))
        print(f'The tactics are -> {name_id}')
        print('=' * 30)
        print()
        return name_id


    def list_sub_techniques(self, tactics) -> list:
        options_id = []
        ids = []
        name = []

        for num in enumerate(tactics):
            options_id.append(num)

        print('This are all the tactics available\n')

        for option in options_id:
            print(option)
        print('=' * 30)
        tactic_option = int(input('Which of the options you want to see the Sub-techniques ? '))
        print('=' * 30)
        req_sub_technique = requests.get(f'{self.link_base}/techniques/{tactics[tactic_option].strip()}')

        bs = bs4.BeautifulSoup(req_sub_technique.content, 'html.parser')
        table = bs.find('table', class_='table table-bordered')
        try:
            hrefs = table.find_all('a',href = re.compile(r'/techniques/T[\d]+/[\d]+/'))
            
            for key, value in enumerate(hrefs):
                if key % 2 ==0:
                    ids.append(value.text.strip())
                else:
                    name.append(value.text.strip())

            concat = zip(ids, name)

            for sub_tech in concat:
                print(sub_tech)
            return ids
        
        except:
            return None


    def sub_techniques_content(self, list_sub_techniques) -> dict:
        mitigation = {}
        
        print('=' * 30)
        
        Sub_techniques_option = int(input('which of the Sub-techniques you wanna see ? '))
        
        print('=' * 30)
        
        sub_id = list_sub_techniques[Sub_techniques_option]
        Sub_techniques_page = requests.get(f'{self.link_base}/techniques/{sub_id[:5]}/{sub_id[6:]}/')
        bs4_sub_techniques = bs4.BeautifulSoup(Sub_techniques_page.content, 'html.parser')
        descripition = bs4_sub_techniques.find('div', {'class': 'description-body'})
        
        print('foi descripition')
        print('=' * 30)
        print(descripition.text)
        
        bs = bs4_sub_techniques.find('table',{'class': 'table table-bordered table-alternate mt-2'})
        header = bs.find('tr').text
        header = header.replace('\n', ' ')
        header = header.split(' ')
        
        del header[0]
        del header[-1]
        
        bs_req_content = bs4_sub_techniques
        tbody = bs_req_content.find_all('tbody')
        tbody = tbody[1].text.strip()
        tbody = tbody.replace('\n\n\n', '#')
        tbody = tbody.split('#')

        for key, value in enumerate(header):
            mitigation[header[key]] = tbody[key]
        print(mitigation)
# getting_tactics,options,tactics,list_sub_techniques, sub_techniques_content
    def main(self):

        getting_tactics = self.getting_tactics()
        option = self.options()
        tactics = self.tactics(getting_tactics, option)
        list_sub_techniques = self.list_sub_techniques(tactics)
        sub_techniques_content = self.sub_techniques_content(list_sub_techniques)
      

Listing_all = listing_tactics()


Listing_all.main()