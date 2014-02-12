"""
settings.py

Settings module that contains proxy, user-agent, and api key information.
"""

user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'
proxy = 'http://h1proxy.frb.org:8080/'

PROXIES = {'http' : proxy}
HEADERS = {'User-Agent' : user_agent}
API_KEY = '053555E15916893815B4B79100C35775'
F_MODE = 'rb+'
