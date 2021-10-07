import xml.etree.ElementTree as ET
tree = ET.parse('https://www.infomoney.com.br/feed/')
root = tree.getroot()