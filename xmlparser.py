import xml.etree.ElementTree as ET 

tree = ET.parse('planet.osm')
db = tree.getroot()

def main():
    print('No longer valid')

def getHighways():
    highways = []
    for child in db.iter('way'):
        way = child
        print("\n id =", way.attrib['id'])
        vals = {'refs': []}
        for element in way.iter('tag'):
            vals[element.attrib['k']] = element.attrib['v']
        for element in way.iter('nd'):
            vals['refs'].append(element.attrib['ref'])
        highways.append(vals)
        print(vals)
    highways

def getNodeByRef(ref):
    ref = str(ref)
    node = {}
    for child in db.iter('node'):
        if child.attrib['id'] == ref:
            node = child
            break
    res = {
        'id' : ref, 
        'lat' : node.attrib['lat'],
        'lon' : node.attrib['lon']
    }
    for child in node:
        res[child.attrib['k']] = child.attrib['v']
    res

def getRelations():
    res = {'members': []}
    for child in db.iter('relation'):
        for member in child.iter('member'):
            res['members'].append({})

def getBuildings():
    buildings = []
    for child in db.iter('way'):
        way = child
        vals = {'node': ''}
        for element in way.iter('tag'):
            vals[element.attrib['k']] = element.attrib['v']
        if not 'building' in vals:
            continue
        print("\n id =", way.attrib['id'])
        for element in way.iter('nd'):
            vals['node'] = element.attrib['ref']
            break
        buildings.append(vals)
        print(vals)
    buildings

def getStreets():
    streets = []
    for child in db.iter('way'):
        way = child
        vals = {'refs': []}
        for element in way.iter('tag'):
            vals[element.attrib['k']] = element.attrib['v']
        if not 'highway' in vals:
            continue
        print("\n id =", way.attrib['id'])
        for element in way.iter('nd'):
            vals['refs'].append(element.attrib['ref'])
        streets.append(vals)
        print(vals)
    streets

if __name__ == "__main__":
    getStreets()