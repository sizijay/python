import urllib
import urllib2

params = {
    'api_key': 'f85ce8a9',
    'api_secret': 'f183d2de',
    'to': '0094719779339',
    'from': 'sizi',
    'text': 'Hello from Nexmo'
}

url = 'https://rest.nexmo.com/sms/json?' + urllib.urlencode(params)

request = urllib2.Request(url)
request.add_header('Accept', 'application/json')
response = urllib2.urlopen(request)
