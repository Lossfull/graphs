import xml.etree.ElementTree as ET 

def lol():
    print('lol')

def main():
    tree = ET.parse('planet.osm')
    db = tree.getroot()
    x = 0
    for child in db:
        if child.tag == 'way':
            way = child
            print("\n id =", way.attrib['id'])
            for element in way:
                atrs = element.attrib
    print(':)')
    255

if __name__ == "__main__":
    main()