import xmlparser
import random

streets = xmlparser.getStreets()

def getGraphList():
    streets = xmlparser.getRoads()
    graph_list = {}
    for street in streets:

        # проверка на одностороннее движение
        oneway = False
        if 'oneway' in street.keys():
            if (street['oneway'] == 'yes') or (street['oneway'] == 'true') or (street['oneway'] == '1'):
                oneway = True
        if 'junction' in street.keys():
            if (street['junction'] == 'roundabout'):
                oneway = True
        if (street['highway'] == 'motorway') or (street['highway'] == 'motorway_link'):
            oneway = True

        # пустой список смежности
        refs = street['refs']
        for node in refs:
            if (not node in graph_list.keys()):
                graph_list[node] = []

        # ребра
        for i in range(len(refs)):
            if (i < len(refs) - 1):
                graph_list[refs[i]].append(refs[i+1])
                if (not oneway):
                    graph_list[refs[i+1]].append(refs[i])

    # веса вершин
    weights = {}
    for v in graph_list.keys():
        weights[v] = random.random() + 1

    print('vse okey :)')
    return (graph_list, weights)



