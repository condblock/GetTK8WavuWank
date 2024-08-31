import json
import glob

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def getchardata(data, charaid, keys):
    charadata = []
    for battle in data:
        if battle['p1_chara_id'] or battle['p2_chara_id'] == charaid:
            charadata.append({key: battle[key] for key in keys})

    return charadata

games = glob.glob('data/all/games_before_*.json')
charaid = 3
keys = ['p1_polaris_id', 'p2_polaris_id', 'p1_chara_id', 'p2_chara_id', 'p1_rank', 'p2_rank', 'winner']

for datas in games:
    with open(f'data/chara/{charaid}/{datas[9:]}', 'w') as f:
        json.dump(getchardata(load_data(datas), charaid, keys), f)