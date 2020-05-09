import xmlparser
import graph


def main():
    # 3 больницы
    # xmlparser.getItemsByAmenity('hospital')
    # '1119810073' - Поликлиника №2 ул. Гагарина 4
    # '2391289850' - Медсанчасть №2 
    # '3488235859' - Роддом имени Семашко

    # 3 дома
    # print(xmlparser.getBuildings())
    # '1305396107' - улица 79-й Гвардейской Дивизии 25/2
    # '3455058975' - Загорная ул. 38
    # '3498617249' - Академический проспект 5/1

    dist_to_obj = {'1305396107':[0,0,0],'3455058975':[0,0,0],'3498617249':[0,0,0]}
    dist_to_bui = {'1119810073':[0,0,0],'2391289850':[0,0,0],'3488235859':[0,0,0]}

    (g,w) = graph.getGraphList()

    nearest_nodes = {}

    nearest_nodes['1119810073'] = graph.NearestNode(g,'1119810073')
    nearest_nodes['2391289850'] = graph.NearestNode(g,'2391289850')
    nearest_nodes['3488235859'] = graph.NearestNode(g,'3488235859')
    nearest_nodes['1305396107'] = graph.NearestNode(g,'1305396107')
    nearest_nodes['3455058975'] = graph.NearestNode(g,'3455058975')
    nearest_nodes['3498617249'] = graph.NearestNode(g,'3498617249')

    (D,Parent) = graph.Dijkstra(g,nearest_nodes['1305396107'])
    dist_to_obj['1305396107'][0] = D[nearest_nodes['1119810073']]
    dist_to_obj['1305396107'][1] = D[nearest_nodes['2391289850']]
    dist_to_obj['1305396107'][2] = D[nearest_nodes['3488235859']]

    (D,Parent) = graph.Dijkstra(g,nearest_nodes['3455058975'])
    dist_to_obj['3455058975'][0] = D[nearest_nodes['1119810073']]
    dist_to_obj['3455058975'][1] = D[nearest_nodes['2391289850']]
    dist_to_obj['3455058975'][2] = D[nearest_nodes['3488235859']]

    (D,Parent) = graph.Dijkstra(g,nearest_nodes['3498617249'])
    dist_to_obj['3498617249'][0] = D[nearest_nodes['1119810073']]
    dist_to_obj['3498617249'][1] = D[nearest_nodes['2391289850']]
    dist_to_obj['3498617249'][2] = D[nearest_nodes['3488235859']]

    (D,Parent) = graph.Dijkstra(g,nearest_nodes['1119810073'])
    dist_to_bui['1119810073'][0] = D[nearest_nodes['1305396107']]
    dist_to_bui['1119810073'][1] = D[nearest_nodes['3455058975']]
    dist_to_bui['1119810073'][2] = D[nearest_nodes['3498617249']]

    (D,Parent) = graph.Dijkstra(g,nearest_nodes['2391289850'])
    dist_to_bui['2391289850'][0] = D[nearest_nodes['1305396107']]
    dist_to_bui['2391289850'][1] = D[nearest_nodes['3455058975']]
    dist_to_bui['2391289850'][2] = D[nearest_nodes['3498617249']]

    (D,Parent) = graph.Dijkstra(g,nearest_nodes['3488235859'])
    dist_to_bui['3488235859'][0] = D[nearest_nodes['1305396107']]
    dist_to_bui['3488235859'][1] = D[nearest_nodes['3455058975']]
    dist_to_bui['3488235859'][2] = D[nearest_nodes['3498617249']]

    print('Расстояния до больниц: ')
    print(dist_to_obj)
    print('Расстояния до домов: ')
    print(dist_to_bui)


if __name__ == "__main__":
    main()