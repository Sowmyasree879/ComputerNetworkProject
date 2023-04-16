import xml.etree.ElementTree as ET

xml_string = '<envelope><method>path</method><node><name>A</name><arg>B</arg><arg>C</arg></node><node><name>B</name><arg>A</arg><arg>C</arg></node><node><name>C</name><arg>B</arg></node></envelope>'

# Parse the XML string
root = ET.fromstring(xml_string)

# Create an empty dictionary to hold the results
result = {}

# Iterate over each node element in the root
for node in root.findall('node'):
    name = node.find('name').text
    args = [arg.text for arg in node.findall('arg')]
    result.setdefault(name,args)

# Print the result
print(result)