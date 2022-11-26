import requests
from find_arbitrage import find_arbitrage
from config import get_config

env = get_config()

response = requests.get(
    env['ODDS_API_HOST']+'/sports/upcoming/odds/',
    params={'regions': 'au', 'markets': 'h2h', 'apiKey': env['ODDS_API_KEY']}
)

find_arbitrage(response.json())
