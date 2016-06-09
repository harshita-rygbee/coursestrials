from pprint import pprint
import pycurl
import ujson
f = open('ids.txt','r')
ids = f.read()
f.close()
ids = ids.split()
basic_url = 'https://api.coursera.org/api/courses.v1'
fields = 'previewLink,language,shortDescription'

curl_instance = pycurl.Curl()
curl_instance.setopt(curl_instance.VERBOSE,True)

print ids
for an_id in ids:
	url = basic_url + '?' + 'ids=' + an_id + '&' + 'fields=' + fields
	print url
	raw_input('url dekho')
	f = open('all_data.txt','ab')
	curl_instance.setopt(curl_instance.URL, url)
	curl_instance.setopt(curl_instance.WRITEDATA,f)
	curl_instance.perform()
	f.close()

