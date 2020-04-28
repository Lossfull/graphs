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
    print(res)

def getRelations():
    res = {'members': []}
    for child in db.iter('relation'):
        for member in child.iter('member'):
            res['members'].append({})

if __name__ == "__main__":
    getNodeByRef('1278222359')