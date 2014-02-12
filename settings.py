"""
settings.py

Settings module that contains proxy, user-agent, and api key information.
"""

#	Set User-Agent and Proxy
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'
proxy = 'http://h1proxy.frb.org:8080/'

# Create constants for header and proxy dictionaries, api key, and file mode.
PROXIES = {'http' : proxy}
HEADERS = {'User-Agent' : user_agent}
API_KEY = '053555E15916893815B4B79100C35775'
F_MODE = 'rb+'

#	Set extensions for archive's web location, the raw data in the archive file, and the json local save location.
extensions = { 'zip' : '.zip', 'text' : '.txt', 'json' : '.json' }

#	Set base download request URL.
url = 'http://api.eia.gov/bulk/'

#	Names of all available datasets and bulk manifest from EIA bulk download facility.
datasets = ['manifest','SEDS','NG','PET','ELEC']

#	Create filenames with extension dictionary and name from manifest.
manifest = datasets[0] + extensions['text']
zip_archive = datasets[2] + extensions['zip']
raw_data = datasets[2] + extensions['text']
json_obj = datasets[2] + extensions['json']
