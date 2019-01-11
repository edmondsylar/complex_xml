import xmltodict
import pymysql
import csv

connection = {
    'host':'localhost',
    'user':'root',
    'passwd':None,
    'database':'sanctions'
}

conn = pymysql.connect(**connection)
cur = conn.cursor()

tables = {
    'firstName':'t_firstname',
    'title':'t_sdntitle',
    'lastName':'t_lastName',
    'programList':'t_programlist',
    'akaList':'t_akaList',
    'addressList':'t_addresses',
    'firstName':'t_sdn_firstname',
    'remarks':'t_sdn_remarks',
    'program':'t_sdn_programList',
    'idType':'t_sdn_idList_idType',
    'idNumber':'t_sdn_idList_idNumber',
    'idCountry':'t_sdn_idList_idCountry',
    'issueDate':'t_sdn_idList_issueDate',
    'expirationDate':'t_sdn_idList_expirationDate',
    'aka':'t_sdn_akaList',
    'address1':'t_sdn_addressList_address1',
    'address2':'t_sdn_addressList_address2',
    'address3':'t_sdn_addressList_address3',
    'city':'t_sdn_addressList_city',
    'stateOrProvince':'t_sdn_addressList_stateorProvince',
    'postalCode':'t_sdn_addressList_postalCode',
    'nationality':'t_sdn_nationalityList',
    'citizenship':'t_sdn_citizenshipList',
    'dateOfBirthItem':'t_sdn_dateOfBirthList',
    'placeOfBirthItem':'t_sdn_placeOfBirthList',
    'vesselInfo':'t_sdn_vesselInfo',
    'callSign':'t_sdn_vesselInfo_callSign',
    'vesselType':'t_sdn_vesselInfo_vesselType',
    'vesselFlag':'t_sdn_vesselInfo_vesselFlag',
    'vesselOwner':'t_sdn_vesselInfo_vesselOwner',
    'vesselTypetonnage':'t_sdn_vesselInfo_tonnage',
    'grossRegisteredTonnage':'t_sdn_vesselInfo_grossRegisteredTonnage'
}

sdn_entry = []

class dbExtarct:
    def __init__(self, filename):
        self.items = []
        self.report = open('report.txt', 'w+')
        with open(filename) as file:
            doc = xmltodict.parse(file.read())

        self.my_obj = doc['sdnList']['sdnEntry']

        for i in range(0, len(self.my_obj)):
            for key, value in self.my_obj[i].items():
                primary_key = self.my_obj[i]['uid']
                if key in tables.keys():
                    if isinstance(value, dict):
                        print ('\n\n{}: \nsdnUid:{}'.format(key, primary_key))
                        self.report.write('\n\n{}: \nsdnUid:{}'.format(key, primary_key))
                        print ('Goes to table {}'.format(tables[key]))
                        # with open('{}.csv'.format(tables[key])) as csvFile:
                            # filednames = []
                        self.report.write('\nGoes to table {}\n'.format(tables[key]))
                        for each in value.values():
                            if isinstance(each, dict):
                                for a, b in each.items():
                                    print ('\t {}: {}'.format(a, b))
                                    self.report.write('\t {}: {}'.format(a, b))
                            else:
                                # print (each)
                                pass
                    # break
                    # pass
                else:
                    pass

test = dbExtarct('test_file.xml')
