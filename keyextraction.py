import xmltodict
import os
from time import sleep

class key_extraciton:
    def __init__(self, filename):
        self.keys = []
        self.key_report = open('keys.txt', 'w+')
        with open(filename) as file:
            doc = xmltodict.parse(file.read())

        self.my_obj = doc['sdnList']['sdnEntry']
        for i in range(0, len(self.my_obj)):
            self.get_keys(self.my_obj[i])

        self.results()

    def get_keys(self, arg):
        if isinstance(arg, dict):
            for key in arg.keys():
                if key in self.keys:
                    pass
                else:
                    self.keys.append(key)
            # self.results()
            for value in arg.values():
                if isinstance(value, dict):
                    self.get_keys(value)
                else:
                    continue
        else:
            pass

    def results(self):
        self.key_report.write('{} keys :\n\t{}'.format(len(self.keys),self.keys))
        print ('complete')
        return(self.keys)

# Completed for OFAC sdnList.
