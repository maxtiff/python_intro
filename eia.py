import json
import urllib.request
from zipfile import ZipFile
import io

#	import urllib error handling
from urllib.error import HTTPError,URLError
from settings import F_MODE


def download_file(base_url, file_url, proxy, header):
	'''(str,str,CONST,CONST)->HTTPResponse

	Return the contents of an HTTP request as response to be used for processing.

	Example:
	>>>download_file('http://api.eia.gov/bulk', '/NG.zip', PROXIES, HEADERS)

	'''
	#	Set base_url
	url = base_url

	#	Set full download url to get the archive file
	full_url = url + file_url

	#	Set proxy
	proxy_support = urllib.request.ProxyHandler(proxies = proxy)
	opener = urllib.request.build_opener(proxy_support)
	urllib.request.install_opener(opener)

	#	Open URL
	req = urllib.request.Request(full_url, data = None, headers = header)
	response = urllib.request.urlopen(req)

	#	Return response in order for save_file function to process archive
	return response



def save_file(data,json_path,response):
	'''(str, str, HTTPResponse)->json_object

	Write the HTTP response to a file for data processing and return the path of that file.
	
	Example:
	>>>save_file('NG.txt','NG.json','http://api.eia.gov/bulk/NG.zip')
	
	'''

	#	Create the json object file in order to write the data.
	f = open(json_path,'wb+')

	#	Read the item in the downloaded archive
	z = ZipFile(io.BytesIO(response.read()))

	#	Write the contents of the item in the archive to a json object.
	for line in z.open(data).readlines():
		f.write(line)
	
	#	Close the json object file.
	f.close()

	return json_path


def decode_json(object):
	'''(json_object)->array

	Convert the downloaded json object to an array of strings.
	'''


