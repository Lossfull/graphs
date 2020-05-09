import xmlparser
import random
import math
from geopy.distance import geodesic


def getGraphList():
    print('Строим граф...')
    streets = xmlparser.getRoads()
    graph_list = {}
    coords = xmlparser.getNodesCoords()
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
                node1_coords = coords[refs[i]]
                node2_coords = coords[refs[i + 1]]
                distance = geodesic(node1_coords, node2_coords).m
                graph_list[refs[i]].append((refs[i+1],distance))
                if (not oneway):
                    graph_list[refs[i+1]].append((refs[i],1))

    # веса вершин
    weights = {}
    for v in graph_list.keys():
        weights[v] = random.random() + 1

    print('Граф построен')
    return (graph_list, weights)


# def Dijkstra_slow(G, start_node):
#     D = {}
#     Parent = {}
#     Matched = []
#     for node in G:
#         D[node] = math.inf
#         Parent[node] = start_node
#     D[start_node] = 0

#     while (len(Matched) < len(D)):
#         min_dist = math.inf
#         for node in G:
#             if (node not in Matched):
#                 if (D[node] < min_dist):
#                     curr_node = node
#                     min_dist = D[node]

#         for child in G[curr_node]:
#             (child_node, distance) = child
#             if (D[child_node] > D[curr_node] + distance):
#                 D[child_node] = D[curr_node] + distance
#                 Parent[child_node] = curr_node
#         Matched.append(curr_node)
#         print(len(Matched))

#     print('nice ^^')
#     return(D,Parent)

def Dijkstra(G, start_node):
    print('Строим дерево кратчайших путей из вершины: ', start_node, '...')
    D = {}
    Parent = {}
    Not_matched = G.copy()
    for node in G:
        D[node] = math.inf
        Parent[node] = '-'
    D[start_node] = 0

    while (len(Not_matched) > 0):
        min_dist = math.inf
        for node in Not_matched:
            if (D[node] <= min_dist):
                curr_node = node
                min_dist = D[node]

        for child in G[curr_node]:
            (child_node, distance) = child
            if (D[child_node] > D[curr_node] + distance):
                D[child_node] = D[curr_node] + distance
                Parent[child_node] = curr_node
        del Not_matched[curr_node]

    print('Дерево построено')
    return (D,Parent)

# G = {'a':[('c',5)], 'b':[('f',20)], 'c':[('b',15),('d',20)], 'd':[('e',23)], 'e':[], 'f':[], 'g':[]}
# (D,Parent) = Dijkstra(G,'a')
# print(D)
# print(Parent)

def NearestNode(G,obj):
    print('Ищем вершину, ближайшую к: ', obj, '...')

    coords = xmlparser.getNodesCoords()
    obj_coords = coords[obj]
    min_dist = math.inf

    for node in G:
        node_coords = coords[node]
        distance = geodesic(node_coords, obj_coords).m
        if (distance < min_dist):
            min_dist = distance
            result = node
    return result




