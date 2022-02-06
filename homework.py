import json
from pprint import pprint
import matplotlib.pyplot as plt


"""
Namu darbas: 
1. Surasti visus objektus, kurius 'records' liste butu id nuo 40 iki 60, galioja ir ju vaikams,
    naudoti rekursija.
2. Su Matplotlib biblioteka atvaizduokite objektu medi su ID kaip antrastemis.
link: https://programmerclick.com/article/4081923774/

self.plot.hlines(y=neuron_y_min, xmin=neuron_x_min, xmax=neuron_x_max, linewidth=2, color='r')
self.plot.hlines(y=neuron_y_max, xmin=neuron_x_min, xmax=neuron_x_max, linewidth=2, color='r')
self.plot.vlines(x=neuron_x_min, ymin=neuron_y_min, ymax=neuron_y_max, linewidth=2, color='r')
self.plot.vlines(x=neuron_x_max, ymin=neuron_y_min, ymax=neuron_y_max, linewidth=2, color='r')

"""


def recursive_search(mega_list, search_ids, plot_, depth=0, x_parent=False):
    res = []
    for nr, object_ in enumerate(mega_list):
        # records_ = object_.get('records', []) or [
        child_records_ = object_['records']
        object_id = object_['id']
        parent_x = x_parent and x_parent or nr * 100
        y_min = depth * 2
        y_max = y_min + 2
        x_min = parent_x
        x_max = parent_x + ((nr - (len(mega_list) / 2)) * 32)
        if object_id in search_ids:
            res.append(object_)

            if depth == 0:
                plot_.vlines(x=x_min, ymin=y_min, ymax=y_max, linewidth=0.125, color='r')
            else:
                x_values = [x_min, x_max]
                y_values = [y_min, y_max]
                plot_.plot(x_values, y_values, linewidth=0.125, color='red')

        else:
            if depth == 0:
                plot_.vlines(x=x_min, ymin=y_min, ymax=y_max, linewidth=0.125, color='g')

        if child_records_ and depth <= 2:
            found_child_records_ = recursive_search(child_records_, search_ids, plot, depth + 1, x_min)
            res.extend(found_child_records_)

    return res


if __name__ == '__main__':
    with open('homework_recursion.json', 'r') as f:
        json_data = json.loads(f.read())

    plot = plt
    figure = plot.figure()
    # pprint(json_data, indent=2)
    # ID 15 records
    rec_15 = recursive_search(json_data, [e for e in range(1, 2)], plot)
    print(len(rec_15))
    plot.show()
