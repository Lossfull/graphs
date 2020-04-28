import xml.etree.ElementTree as ET 

def main():
    tree = ET.parse('planet.osm')
    db = tree.getroot()
    x = 0
    highways = []
    for child in db:
        if child.tag == 'way':
            way = child
            print("\n id =", way.attrib['id'])
            vals = {}
            for element in way.iter('tag'):
                vals[element.attrib['k']] = element.attrib['v']
                #print(, element.attrib['v'])
            highways.append(vals)
            print(vals)
    highways

if __name__ == "__main__":
    main()