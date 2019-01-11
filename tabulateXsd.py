import xmltodict

with open('this.xsd') as file:
    doc = xmltodict.parse(file.read())
    obj = doc['xs:schema']['xs:element']

for each in obj:
    print(each)
    print(type(each))

# print(type(doc))
