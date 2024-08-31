import requests
import json
import time
import glob

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def append_if_not_exists(list, id):
    exists = any(d['chara_id'] == id for d in list)
    if not exists:
        list.append({'chara_id': id, 'wins': 0, 'loses': 0})

def find_index(list, id):
    for index, dictionary in enumerate(list):
        if dictionary.get('chara_id') == id:
            return index

def getchardata(data, charid, dumpkeys):
    chardata = []
    for battle in data:
        if battle['p1_chara_id'] or battle['p2_chara_id'] == charid:
            for keys in dumpkeys:
                del data[keys]
            chardata.append({})
    return chardata
def getwinrate(data, winlose):
    games = 0
    for battle in data:
        p1_chara_id = battle['p1_chara_id']
        p2_chara_id = battle['p2_chara_id']
        winner = battle['winner']

        append_if_not_exists(winlose, p1_chara_id)
        append_if_not_exists(winlose, p2_chara_id)

        p1_chara_idx = find_index(winlose, p1_chara_id)
        p2_chara_idx = find_index(winlose, p2_chara_id)

        if winner == 1:
            winlose[p1_chara_idx]['wins'] += 1
            winlose[p2_chara_idx]['loses'] += 1
        if winner == 2:
            winlose[p1_chara_idx]['loses'] += 1
            winlose[p2_chara_idx]['wins'] += 1
        games += 1
    for chara in winlose:
        chara['winrate'] = chara['wins'] / ( chara['wins'] + chara['loses'] )
    return games

games = glob.glob('data/all/games_before_*.json')

for data in games:



rep = 30
games = 0
start_time = int(time.time())
winlose: list = []

for i in range(rep):
    url = f'https://wank.wavu.wiki/api/replays?before={start_time-(700*i)}'
    response = requests.get(url).json()
    games += getwinrate(response, winlose)
    winlose = sorted(winlose, key=lambda x:x['chara_id'])
    with open('data/replays.json', 'w') as f:
        json.dump({'games': games, 'rates': winlose}, f)
    print(i, games)