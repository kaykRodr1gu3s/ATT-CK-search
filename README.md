# ATT&CK-search
## Overview

This project aims to gather comprehensive data on Tactics, Techniques, and their respective Sub-Techniques from [Mitre](https://attack.mitre.org/matrices/enterprise/) through web scraping and subsequent data analysis. The collected data includes the name, description, and informational details associated with each Tactic and Technique.

For Tactic information, we collect the name, description, and any additional relevant details available in the form of information cards.

For Techniques, we gather the name, ID, associated Sub-Technique IDs, platform compatibility, and version information.

The collected data is organized and stored in YAML files for easy access and readability. Each Tactic has its own YAML file containing its details, while each Technique is represented by a separate YAML file.

The project utilizes web scraping techniques to extract data from online sources, followed by data analysis to ensure data integrity and completeness.
---

### Index
1 - [Overview](#Overview)

2 - [Requisites](#Requisites)

3 - [Usage](#Usage)

4 - [Contribution](#Contribution)

5 - [Contact](#Contact)

### Requisites

Before using the code, make sure to install the required Python libraries using the following commands:

```bash
pip install bs4
pip install PyYAML
pip install requests
pip install pandas
```

---

### Usage

By default, all data will be saved in the "tactics" directory.
![image](https://github.com/kaykRodr1gu3s/Mitre-mapper/assets/110197812/be61af8f-82db-4d5d-9cea-9dbc5d22c85c)


If you wish to overwrite the data, delete the existing files in the "tactics" directory and the "techniques" folder.

![image](https://github.com/kaykRodr1gu3s/Mitre-mapper/assets/110197812/fdc4c4fa-99cb-4bb4-b91e-91779641841c)


Upon executing the code, all data will be resaved accordingly.

---

### Contribution
 1. Fork the repository.
 2. Create a branch for your contribution: `git checkout -b feature-nova`.
 3. Make the desired changes and commit: `git commit -m "Add new functionality"`.
 4. Push to your branch: `git push origin new-feature`.
 5. Open a pull request.


## Contact

- Linkedin: [Kayk Rodrigues](https://www.linkedin.com/in/kayk-rodrigues-504a03273)
- Telegram: [Kayk Rodrigues](https://t.me/kaykRodrigues)


