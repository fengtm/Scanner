import requests
r = requests.get('https://api.raydium.io/v2/ammV3/ammPools')
print(r.json())
