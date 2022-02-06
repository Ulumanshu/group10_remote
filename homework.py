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


def recursive_search(mega_list, search_ids, plot_, depth=0, x_parent=0.00):
    res = []
    for nr, object_ in enumerate(mega_list):
        child_records_ = object_['records']
        object_id = object_['id']
        parent_x = x_parent and x_parent or nr * 1000
        y_min = depth * 2
        y_max = y_min + 2
        x_min = parent_x
        x_max = x_min + ((nr - (len(mega_list) / 2)) * 1200)
        x_values = [x_min, x_max]
        y_values = [y_min, y_max]
        if object_id in search_ids:
            res.append(object_)
            if depth == 0:
                plot_.vlines(
                    x=x_min,
                    ymin=y_min,
                    ymax=y_max,
                    linewidth=0.125,
                    color='red',
                    label=f'{object_id}'
                )
            else:
                plot_.plot(
                    x_values,
                    y_values,
                    linewidth=0.125,
                    color='red',
                    label=f'{object_id}'
                )

        elif [rec for rec in child_records_ if rec['id'] in search_ids]:
            if depth == 0:
                plot_.vlines(
                    x=x_min,
                    ymin=y_min,
                    ymax=y_max,
                    linewidth=0.125,
                    color='blue',
                    label=f'{object_id}'
                )
            else:
                plot_.plot(
                    x_values,
                    y_values,
                    linewidth=0.125,
                    color='blue',
                    label=f'{object_id}'
                )

        else:
            if depth == 0:
                plot_.vlines(
                    x=x_min,
                    ymin=y_min,
                    ymax=y_max,
                    linewidth=0.125,
                    color='g',
                    label=f'{object_id}',
                )

        if child_records_ and depth <= 4:
            child_x = x_max
            if depth == 0:
                child_x = x_min
            found_child_records_ = recursive_search(
                child_records_, search_ids, plot_,
                depth=depth + 1,
                x_parent=child_x,
            )
            res.extend(found_child_records_)

    return res


if __name__ == '__main__':
    with open('homework_recursion.json', 'r') as f:
        json_data = json.loads(f.read())

    plot = plt
    plot.rcParams["figure.figsize"] = (40, 10)
    figure = plot.figure()
    # pprint(json_data, indent=2)
    # ID 15 records
    rec_1 = recursive_search(json_data, [e for e in range(1, 2)], plot)
    print(len(rec_1))
    plot.show()
