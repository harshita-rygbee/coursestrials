'''So we are trying to collect data from coursera using the catalog api.'''
from pprint import pprint
import pycurl
import ujson
# url = "https://api.coursera.org/api/instructors.v1/5377163?includes=instructorIds,partnerIds&fields=instructorIds,department,partnerIds"
basic_url = 'https://api.coursera.org/api/courses.v1'
start = 0
limit = 1
fields = 'previewLink,language,shortDescription'
# url = "https://api.coursera.org/api/courses.v1?ids=Z3yHdBVBEeWvmQrN_lODCw,v1-3,Gtv4Xb1-EeS-ViIACwYKVQ&fields=language,shortDescription,previewLink,specializations,s12nIds"
ids = []
curl_instance = pycurl.Curl()
curl_instance.setopt(curl_instance.VERBOSE,True)

#Opening a file to read:

while True:
	f = open('jsons.txt','w')
	url = basic_url# + '?' + 'start=' + str(start) + '&' + 'limit=' + str(limit)
	curl_instance.setopt(curl_instance.URL, url)
	curl_instance.setopt(curl_instance.WRITEDATA,f)
	curl_instance.perform()
	f.close()
	f = open('jsons.txt','r')
	body = f.read()
	print body
	raw_input('body dekho')
	body_json = ujson.loads(body)
	pprint(body_json)
	f.close()
	start = body_json['paging']['next']
	for course in body_json['elements']:
		ids.append(course['id'])
	if start == u'2':
		break
	print ids,'start=',start
	raw_input('ids dekho')



ids_string = ','.join(id for id in ids)
print ids_string
raw_input('ids dekho')
url = basic_url + '?' + 'ids=' + ids_string + '&' + 'fields=' + fields
# url = 'https://api.coursera.org/api/courses.v1&ids=v1-228,69Bku0KoEeWZtA4u62x6lQ&fields=previewLink,language,shortDescription'
print url
raw_input('url dekho')
f2 = open('final.txt','wb+')
	# url = basic_url + '?' + 'start=' + str(start) + '&' + 'limit=' + str(limit)
curl_instance.setopt(curl_instance.URL, url)
curl_instance.setopt(curl_instance.WRITEDATA,f2)
curl_instance.perform()
body2 = f2.read()
print body2
raw_input('body dekho')
body2_json = ujson.loads(body2)
pprint(body2_json)

'''Now the problem is, this allows you to paginate through chunks of results, but these results do not have all the fields'''

curl_instance.close()


#References:
# For pagination: curl "https://api.coursera.org/api/courses.v1?start=300&limit=10"
# For requesting more fields: curl "https://api.coursera.org/api/courses.v1?ids=v1-3,Gtv4Xb1-EeS-ViIACwYKVQ&fields=language,shortDescription"

# while True: