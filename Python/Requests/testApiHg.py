import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

link = 'https://api.hgbrasil.com/finance'

req = requests.get(link, headers=headers)
req_json = req.json()

dollar = req_json['results']['currencies']['USD']
euro = req_json['results']['currencies']['EUR']
bitCoin = req_json['results']['currencies']['BTC']
