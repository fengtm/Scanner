import requests
import json

r = requests.get('https://api.raydium.io/v2/ammV3/ammPools')
body = r.json()

data = body['data'][0]

id = data['id']
mintProgramIdA = data['mintProgramIdA']

print('id: ' + id)
print('mintProgramIdA: ' + mintProgramIdA)

# sample data
#{'id': '2QdhepnKRTLjjSqPL1PtKNwqrUkoLee5Gqs8bvZhRdMv', 'mintProgramIdA': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA', 'mintProgramIdB': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA', 'mintA': 'So11111111111111111111111111111111111111112', 'mintB': 'EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v', 'vaultA': 'E2BcoCeJLTa27mAXDA4xwEq3pBUcyH6XXEHYk4KvKYTv', 'vaultB': '4d35yC7C8zhCDec7JbPptL9SEb4NUddKHxURgmvD8hfo', 'mintDecimalsA': 9, 'mintDecimalsB': 6, 'ammConfig': {'id': 'HfERMT5DRA6C1TAqecrJQFpmkf3wsWTMncqnj3RDg5aw', 'index': 2, 'protocolFeeRate': 120000, 'tradeFeeRate': 500, 'tickSpacing': 10, 'fundFeeRate': 40000, 'fundOwner': 'FundHfY8oo8J9KYGyfXFFuQCHe7Z1VBNmsj84eMcdYs4', 'description': 'Best for wider ranges'}, 'rewardInfos': [{'mint': '4k3Dyjzvzp8eMZWUXbBCjEvwSkkk59S5iCNLY3QrkX6R', 'programId': 'TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA'}], 'tvl': 5579312.463303968, 'day': {'volume': 15119213.880660998, 'volumeFee': 6350.069829877623, 'feeA': 17.489355227468877, 'feeB': 3064.0691586670177, 'feeApr': 41.35, 'rewardApr': {'A': 30.47, 'B': 0, 'C': 0}, 'apr': 71.82, 'priceMin': 179.77528089887642, 'priceMax': 191.61914655601356}, 'week': {'volume': 49547836.998745024, 'volumeFee': 20810.091539472905, 'feeA': 55.01267386241843, 'feeB': 10347.940696731122, 'feeApr': 19.36, 'rewardApr': {'A': 30.47, 'B': 0, 'C': 0}, 'apr': 49.83, 'priceMin': 168.22429906542055, 'priceMax': 222.22222222222223}, 'month': {'volume': 734254916.1184078, 'volumeFee': 308387.06476973154, 'feeA': 974.8018211048155, 'feeB': 154436.98879042667, 'feeApr': 66.95, 'rewardApr': {'A': 30.47, 'B': 0, 'C': 0}, 'apr': 97.42, 'priceMin': 113.20754716981132, 'priceMax': 222.22222222222223}, 'lookupTableAccount': 'EKbdivk32nQdxzP1Z7AUMjsSTgCtoeQTsKzpQ8Rpstcw', 'openTime': 0, 'price': 184.68875587689692}
