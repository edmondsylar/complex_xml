import xmltodict

with open('test_file.xml') as file:
    doc = xmltodict.parse(file.read())

# print (len(doc))
# for each in doc:
#     my_obj = each[each]
#     for all in my_obj:
#         print (all)
my_dict = {
    'name':'edmond',
    'level':'expert',
    'age':20
}

keys = []

def samples(arg):
    if isinstance(arg, dict):
        for key in arg.keys():
            keys.append(key)
    print (keys)


samples(my_dict)
