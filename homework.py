import json
from pprint import pprint


"""
Namu darbas: 
1. Surasti visus objektus, kurius 'records' liste butu id nuo 40 iki 60, galioja ir ju vaikams,
    naudoti rekursija.
2. Su Matplotlib biblioteka atvaizduokite objektu medi su ID kaip antrastemis.
link: https://programmerclick.com/article/4081923774/
"""


def recursive_search(mega_list, search_ids, depth=0):
    res = []
    for nr, object_ in enumerate(mega_list):
        # records_ = object_.get('records', []) or [
        child_records_ = object_['records']
        object_id = object_['id']
        if object_id in search_ids:
            res.append(object_)

        if child_records_ and depth <= 4:
            found_child_records_ = recursive_search(child_records_, search_ids, depth + 1)
            res.extend(found_child_records_)

    return res


if __name__ == '__main__':
    with open('homework_recursion.json', 'r') as f:
        json_data = json.loads(f.read())

    # pprint(json_data, indent=2)
    # ID 15 records
    rec_15 = recursive_search(json_data, [e for e in range(40, 61)])
    print(len(rec_15))
