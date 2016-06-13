'''So we are trying to collect data from coursera using the catalog api.'''
from pprint import pprint
import pycurl
import ujson
# url = "https://api.coursera.org/api/instructors.v1/5377163?includes=instructorIds,partnerIds&fields=instructorIds,department,partnerIds"
basic_url = 'https://api.coursera.org/api/courses.v1'
start = 0
limit = 100
fields = 'previewLink,description,primaryLanguages,subtitleLanguages,startDate'
includes = 'partnerIds,specializations,instructorIds'
# url = "https://api.coursera.org/api/courses.v1?ids=Z3yHdBVBEeWvmQrN_lODCw,v1-3,Gtv4Xb1-EeS-ViIACwYKVQ&fields=language,shortDescription,previewLink,specializations,s12nIds"
curl_instance = pycurl.Curl()
curl_instance.setopt(curl_instance.VERBOSE,True)
'''Change the start and total variables. Reads all the required data to all_data_courses.txt'''
#Opening a file to read:
f2 = open('all_data_courses.txt','ab')
while True:
	ids = []
	f = open('jsons.txt','w')
	url = basic_url + '?' + 'start=' + str(start) + '&' + 'limit=' + str(limit)
	curl_instance.setopt(curl_instance.URL, url)
	curl_instance.setopt(curl_instance.WRITEDATA,f)
	curl_instance.perform()
	f.close()
	f = open('jsons.txt','r')
	body = f.read()
	print body
	# raw_input('body dekho')
	body_json = ujson.loads(body)
	pprint(body_json)
	f.close()
	start = body_json['paging']['next']
	total = 100
	# total = body_json['paging']['total']
	for course in body_json['elements']:
		ids.append(course['id'])
	print ids,'start=',start
	# raw_input('ids dekho')
	ids1 = ids[:20]
	ids2 = ids[20:40]
	ids3 = ids[40:60]
	ids4 = ids[60:80]
	ids5 = ids[80:]
	id_strings = []
	id_strings.append(','.join(i for i in ids1))
	id_strings.append(','.join(i for i in ids2))
	id_strings.append(','.join(i for i in ids3))
	id_strings.append(','.join(i for i in ids4))
	id_strings.append(','.join(i for i in ids5))
	print ids
	for an_id in id_strings:
		url = basic_url + '?' + 'ids=' + an_id + '&' + 'includes=' + includes + '&' + 'fields=' + fields + ',' + includes
		print url
		# raw_input('url dekho')
		curl_instance.setopt(curl_instance.URL, url)
		curl_instance.setopt(curl_instance.WRITEDATA,f2)
		curl_instance.perform()
	if int(start) > int(total):
		print 'start and total',start, total
		# raw_input('start and total')
		break
f.close()
curl_instance.close()
# website example:https://api.coursera.org/api/courses.v1?ids=Z3yHdBVBEeWvmQrN_lODCw,v1-3,Gtv4Xb1-EeS-ViIACwYKVQ&fields=language,shortDescription,previewLink,specializations,s12nIds
# my attempt: https://api.coursera.org/api/courses.v1?ids=v1-228&fields=previewLink,language,shortDescription
# v1-3
# https://api.coursera.org/api/courses.v1?ids=v1-3,v1-228&fields=previewLink,language,shortDescription
