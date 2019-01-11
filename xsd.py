import requests
import xmltodict

def xsd_extraxt(url, name):
    resp = requests.get(url)
    # print (resp.content)
    cont_type = (resp.headers.get('content-type'))
    print (cont_type)
    open(name, 'wb').write(resp.content)


# xsd_extraxt('https://www.treasury.gov/resource-center/sanctions/SDN-List/Documents/sdn.xsd', 'this.xml')
