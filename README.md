# ATT&CK-search
## Overview


This tool enables you to search for tactics, techniques, and sub-techniques in the MITRE ATT&CK matrix.

---

### Index
1 - [Overview](#Overview)

2 - [Requisites](#Requisites)

3 - [How to use](#How-to-use)


### Requisites

Before using the code, make sure to install the required Python libraries using the following commands:

```bash
pip install bs4
pip install PyYAML
pip install requests
```

---

### How to Use

After to execute the code:

* Select the desired tactic for the search.
* Choose the technique within the selected tactic.
+ + if the technique has sub-techniques, you will be prompted to choose a sub-technique.

+ + Select the sub-technique.
  
+ If the technique has no sub-techniques, the code will finish.

Once all options (tactics, techniques, and sub-techniques) are finalized, the output will be displayed in your terminal. You will also have the option to save this output to a YAML file.
[Example](https://github.com/kaykRodr1gu3s/ATTCK-search/blob/main/Enterprise/tactics/example.yaml) YAML File


### Contribution
 1. Fork the repository.
 2. Create a branch for your contribution: `git checkout -b feature-nova`.
 3. Make the desired changes and commit: `git commit -m "Add new functionality"`.
 4. Push to your branch: `git push origin new-feature`.
 5. Open a pull request.


## Contact

- Linkedin: [Kayk Rodrigues](https://www.linkedin.com/in/kayk-rodrigues-504a03273)
- Telegram: [Kayk Rodrigues](https://t.me/kaykRodrigues)


