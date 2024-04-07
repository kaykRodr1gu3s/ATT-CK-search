import requests
import bs4 
import re


from Tools import techniques
from Tools import file


class Tactic:
    """
    This class will make a request to https://attack.mitre.org and collect all the tactics along with their information, such as description, ID, creation date, and last modified date.    
    """
    def __init__(self) -> None:
        self.link_base = 'https://attack.mitre.org'
        self.tactic_link = []
        self.tactic_name = []
        self.tactic_info = {}
        self.techniques_id = []


    def tactic_tracker(self):
        """
        This function will collect all the tactics names and ids.
        """
        req = requests.get(f'{self.link_base}/tactics/enterprise/')
        bs = bs4.BeautifulSoup(req.content, 'html.parser')
        bs = bs.find('table', class_='table table-bordered table-alternate mt-2')
        bs4_tactics = bs.find_all('a', href=re.compile(r'/tactics/TA[\d]+'))

        for key, value in enumerate(bs4_tactics):
            if key % 2 == 0:
                self.tactic_link.append(value.text)
            else:
                self.tactic_name.append(value.text)


    def info_tracker(self, link):
        """
        This function will collect information on tactics, including tactic name, description, ID, creation date, last modified date, and associated technique IDs.
        """
        for tactic in link:
            Tactic_information = {}
            req = requests.get(f"{self.link_base}/tactics/{tactic}")            
            bs = bs4.BeautifulSoup(req.content, "html.parser")
            name = bs.find("h1").text.replace("\n", "").strip()
            
            information = bs.find("div", class_="card-body")
            information = information.text.replace(u'\xa0', '')
            information = information.split('\n')

            description= bs.find("div", class_="description-body")
            
            del information[0]
            del information[-1]
    
            technique_id = bs.find_all("td", {"colspan": "2"})
            del technique_id[0]
            
            for tech_id in technique_id:
                tech_id = tech_id.text.replace('\n', '').strip()
                if tech_id not in self.techniques_id: 
                    self.techniques_id.append(tech_id)
                else:
                    continue
                
            Tactic_information["Tactic Name"] = name
            Tactic_information["Description"] = [description.text.replace("\\", "").replace("\n", "")]
            Tactic_information["Information"] = information

            self.tactic_info[name] = Tactic_information


print("Collecting")        

tactic = Tactic()
tactic.tactic_tracker()
tactic.info_tracker(tactic.tactic_link)



technique = techniques.Techniques_tracker()
technique.collecting(tactic.techniques_id)


file_writer = file.file_writer()
file_writer.file_creator(tactic.tactic_info, technique.all_infos)

