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
url = "https://api.coursera.org/api/courses.v1?ids=Z3yHdBVBEeWvmQrN_lODCw,v1-3,Gtv4Xb1-EeS-ViIACwYKVQ&fields=language,shortDescription,previewLink"

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
'''Now the problem is, this allows you to paginate through chunks of results, but these results do not have all the fields'''
#References:
# For pagination: curl "https://api.coursera.org/api/courses.v1?start=300&limit=10"
# For requesting more fields: curl "https://api.coursera.org/api/courses.v1?ids=v1-3,Gtv4Xb1-EeS-ViIACwYKVQ&fields=language,shortDescription"

