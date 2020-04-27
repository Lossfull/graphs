import xml.etree.ElementTree as ET 

def main():
    tree = ET.parse('planet.osm')
    root = tree.getroot()
    x = 0
    for child in root:
        if child.tag == 'way':
            x = x + 1
    print(x)

if __name__ == "__main__":
    main()