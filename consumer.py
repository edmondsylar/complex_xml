from keyextraction import key_extraciton
import pymysql
from time import sleep

test = key_extraciton('test_file.xml')
print (type(test))
for each in test:
    print (each)
