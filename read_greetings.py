import xml.etree.ElementTree as ET

tree = ET.parse('greetings.xml')
root = tree.getroot()
for greeting in root.findall('{openstax.org}greeting'):
    prefix = greeting.find('{openstax.org}prefix')
    target = greeting.find('{openstax.org}target')
    print(prefix.text.title() + ', ' + target.text.title() + '!')
