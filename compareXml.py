import xml.etree.ElementTree as ET
import re

def sort_xml(element):
    # If the element has children, sort its children
    if len(element) > 0:
        element[:] = sorted(element, key=lambda x: x.tag)
        for child in element:
            sort_xml(child)
    return element



# Load the first XML object
tree1 = ET.parse('local.xml')
root1 = tree1.getroot()

# Sort the keys of the XML tree and its nested elements
sort_xml(root1)

# Write the sorted XML tree to the file
tree1.write('local.xml')

# Load the second XML object
tree2 = ET.parse('dev.xml')
root2 = tree2.getroot()

# Sort the keys of the XML tree and its nested elements
sort_xml(root2)

# Write the sorted XML tree to the file
tree2.write('dev.xml')
