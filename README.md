# ATT&CK-search

Pesquisa na matrize enterprise: táticas, técnicas e sub-técnicas no MITRE ATT&CK.

---
## Pré-requisitos
será necessário instalar algumas bibliotecas python: bs4, request e PyYAML
```bash
pip install bs4
pip install PyYAML
pip install requests
```

# Como usar 
Para usar este código é muito simples, todas as instalações já estão feitas.
Para começar a pesquisa, execute o código 

 
 * selecione a tática desejada para a pesquisa
 * selecione a técnica desejada
 
 _se esta técnica possuir sub-tecnicas, será solicitado uma opção para fazer uma pesquisa nesta sub-técnicas_
   * selecione a sub-técnica
 
 _se a técnica não possuir sub-técnicas, o código ira finalizar_

Quando o todas as opções(táticas, técnicas, e sub-técnicas) forem finalizada, você terá um output em seu terminal, e será dada a opção de salvar este output em um arquivo .yaml.


---

Para ver um exemplo de arquivo .yaml [clique aqui](https://github.com/kaykRodr1gu3s/ATTCK-search/blob/main/Mitre_ATTCK/example.yaml)
