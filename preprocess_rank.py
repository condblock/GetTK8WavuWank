import json
import glob

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def getrankdata(data, keys):
    charadata = []
    for battle in data:
        if battle['battle_type'] == 2:
            charadata.append({key: battle[key] for key in keys})

    return charadata

games = glob.glob('data/all/games_before_*.json')
keys = ['p1_rank', 'p2_rank']

for datas in games:
    with open(f'data/rank/{datas[9:]}', 'w') as f:
        json.dump(getrankdata(load_data(datas), keys), f)