import xml.etree.ElementTree as ET 

def main():
    tree = ET.parse('planet.osm')
    root = tree.getroot()
    for child in root:
        print(child.tag)

if __name__ == "__main__":
    main()