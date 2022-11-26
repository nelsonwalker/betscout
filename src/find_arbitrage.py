def calculate_ratios(outcomes: dict):
    highest_likelihood = min([x['price'] for x in outcomes.values()])
    result = {}
    for key in outcomes:
        result[key] = highest_likelihood / outcomes[key]['price']
    return result


def find_arbitrage(json):
    for event in json:
        bookie_index = 0
        outcomes = {}
        for bookie in event['bookmakers']:
            h2h_market = [x for x in bookie['markets'] if x['key'] == 'h2h'][0]
            for outcome in h2h_market['outcomes']:
                name = outcome['name']
                if bookie_index == 0:
                    outcomes[name] = {'price': outcome['price'],
                                      'bookie': bookie['title']}
                if outcome['price'] > outcomes[name]['price']:
                    outcomes[name] = {'price': outcome['price'],
                                      'bookie': bookie['title']}
            bookie_index += 1
        odds = [1 / x['price'] for x in outcomes.values()]
        if sum(odds) < 1:
            print('Sport: ' + event['sport_title'])
            print(outcomes)
            print(calculate_ratios(outcomes))
