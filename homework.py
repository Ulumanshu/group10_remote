import json
from pprint import pprint


"""
Namu darbas: 
1. Surasti visus objektus, kurius 'records' liste butu id nuo 40 iki 60, galioja ir ju vaikams,
    naudoti rekursija.
2. Su Matplotlib biblioteka atvaizduokite objektu medi su ID kaip antrastemis.
link: https://programmerclick.com/article/4081923774/
"""

if __name__ == '__main__':
    with open('homework_recursion.json', 'r') as f:
        json_data = json.loads(f.read())

    pprint(json_data, indent=2)
