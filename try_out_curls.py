'''So we are trying to collect data from coursera using the catalog api.'''
from pprint import pprint
import pycurl
from StringIO import StringIO
import ujson

basic_url = 'https://api.coursera.org/api/courses.v1'
start = 0
limit = 100
fields = 'language,shortDescription'
# url = basic_url + '?' + 'start=' + str(start) + '&' + 'limit=' + str(limit) + '&' + 'fields=' + fields
# url = "https://api.coursera.org/api/courses.v1?ids=Z3yHdBVBEeWvmQrN_lODCw,v1-3,Gtv4Xb1-EeS-ViIACwYKVQ&fields=language,shortDescription,previewLink"
url = "https://api.coursera.org/api/courses.v1?ids=v1-228,v1-3,69Bku0KoEeWZtA4u62x6lQ,0HiU7Oe4EeWTAQ4yevf_oQ,5zjIsJq-EeW_wArffOXkOw,v9CQdBkhEeWjrA6seF25aw,QgmoVdT2EeSlhSIACx2EBw,QTTRdG3vEeWG0w42Sx-Gkw,v1-1355,5uXCfFu2EeSU0SIACxCMgg,Rr2thkIKEeWZtA4u62x6lQ,rajsT7UJEeWl_hJObLDVwQ,lfKT5sS3EeWhPQ55lNYVVQ,v1-1250,POZJ3uOtEeSoXCIACw4Gzg,ugSnwH9hEeSiIiIAC3lQMQ,rc5KG0aUEeWG1w6arGoEIQ,gpAI9GK4EeWFkQ7sUCFGVQ,v1-640,Kzg9QkDxEeWZtA4u62x6lQ,tEqImn2kEeWb-BLhFdaGww&fields=previewLink,language,shortDescription"
print url
raw_input('url dekho')
bufferr = StringIO()
curl_instance = pycurl.Curl()
curl_instance.setopt(curl_instance.URL, url)
curl_instance.setopt(curl_instance.WRITEDATA,bufferr)
curl_instance.setopt(curl_instance.VERBOSE,True)
curl_instance.perform()
curl_instance.close()
body = bufferr.getvalue()
print body
body_json = ujson.loads(body)
pprint(body_json)
start = body_json['paging']['next']