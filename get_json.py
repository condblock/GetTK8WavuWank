import requests
import json
import time

rep = 100
start_time = (int(time.time())//700)*700
# start_time = ~~~

for i in range(rep):
    url = f'https://wank.wavu.wiki/api/replays?before={start_time-(700*i)}'
    response = requests.get(url).json()
    with open(f'data/all/games_before_{start_time-(700*i)}.json', 'w') as f:
        json.dump(response, f)
    print(i)