import xmltodict
import os
from time import sleep

class file_sort:
    def __init__(self, filename):
        self.report = open('report.csv', 'w+')
        with open (filename) as fd:
            doc = xmltodict.parse(fd.read())

        self.my_obj = doc['sdnList']['sdnEntry']
        for i in range(0, len(self.my_obj)):
            self.get_info(self.my_obj[i])

    def get_info(self, arg):
        of_type = type(arg)
        lenght = len(arg)
        name = arg['lastName']
        self.report.write('\n \n{}\n'.format(name))

        if isinstance(arg, dict):
            self.get_keys(arg)
        else:
            pass

    def get_keys(self, arg):
        keys = []
        for key in arg.keys():
            keys.append(key)
        self.report.write('\t {}\n'.format(keys))

        values = []
        for val in arg.values():
            values.append(val)

        self.report.write('\t {}\n\n'.format(values))
        for any in arg.values():
            if isinstance(any, dict):
                self.more_dicts(any)

    def more_dicts(self, arg):
        keys = []
        for key in arg.keys():
            keys.append(key)

        self.report.write('\n\t {}\n'.format(keys))
        for each in keys:
            self.report.write('\t {} : {}\n'.format(each, arg[each]))

        for value in arg.values():
            if isinstance(value, dict):
                # self.report.write('\t')
                self.more_dicts(value)
            else:
                pass

test = file_sort('test_file.xml')
