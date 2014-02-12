"""

Download.py


"""
#	Import functions from EIA module
from eia import *

#	import settings file
from settings import * 

#	Set base download request URL
link = 'http://api.eia.gov/bulk/'

#	Set manifest url
manifest = 'manifest.txt'

#	Set base name for downloads
filename = 'NG'

#	Set extensions to archive's web location, raw data local download location, and json local save location.
extensions = { 'zip' : '.zip', }

z_ext = '.zip'
d_ext = '.txt'
j_ext = '.json'
zip_archive = filename + z_ext
raw_data = filename + d_ext
json_obj = filename + j_ext


data = download_file(link,zip_archive,PROXIES,HEADERS)
save_file(raw_data, json_obj, data)
decode_json(json_obj)
