import json
import glob
import matplotlib.pyplot as plt

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def exists(list, chara_id):
    return any(d['chara_id'] == chara_id for d in list)

def find_index(list, id):
    for index, dictionary in enumerate(list):
        if dictionary.get('chara_id') == id:
            return index

def get_winlose(data, winlose):
    for game in data:
        if game['p1_rank'] and game['p2_rank'] >= 27:
            if game['p1_chara_id'] == 3:
                if not exists(winlose, game['p2_chara_id']):
                    winlose.append({'chara_id': game['p2_chara_id'], 'wins': 0, 'loses': 0})
                index = find_index(winlose, game['p2_chara_id'])
                if game['winner'] == 1:
                    winlose[index]['wins'] += 1
                else:
                    winlose[index]['loses'] += 1
            else:
                if not exists(winlose, game['p1_chara_id']):
                    winlose.append({'chara_id': game['p1_chara_id'], 'wins': 0, 'loses': 0})
                index = find_index(winlose, game['p1_chara_id'])
                if game['winner'] == 1:
                    winlose[index]['wins'] += 1
                else:
                    winlose[index]['loses'] += 1

                


def get_rank(data, doneID, ranks):
    for game in data:
        if game['p1_chara_id'] == 3:
            if not game['p1_polaris_id'] in doneID:
                doneID.append(game['p1_polaris_id'])
                ranks[game['p1_rank']] += 1
        else:
            if not game['p2_polaris_id'] in doneID:
                doneID.append(game['p2_polaris_id'])
                ranks[game['p2_rank']] += 1

            

charaid = 3
games = glob.glob(f'data/chara/{charaid}/games_before_*.json')
doneID = []
winlose = []
ranks = [0 for i in range(30)]

for datas in games:
    data = load_data(datas)
    get_winlose(data, winlose)
    get_rank(data, doneID, ranks)

winlose = sorted(winlose, key=lambda x:x['chara_id'])

print(winlose)

chara_ids = [winlose.index(item) for item in winlose]
winrates = [item["wins"]/(item["wins"]+item["loses"]) for item in winlose]

plt.figure(figsize=(10, 5))
plt.xticks(range(40))
plt.plot(chara_ids, winrates, marker='o', linestyle='', color='b')
plt.xlabel('Character ID')
plt.ylabel('Winrate')
plt.title('Winrate by Chara ID')
plt.grid(True)
plt.show()  

rankrates = [ranks[i]/len(doneID) for i in range(30)]


plt.figure(figsize=(10, 5))
plt.xticks(range(40))
plt.plot([i for i in range(30)], rankrates, marker='o', linestyle='', color='b')
plt.xlabel('Character ID')
plt.ylabel('Winrate')
plt.title('Winrate by Chara ID')
plt.grid(True)
plt.show()  

total=0
for item in winlose:
    total += item['wins']+item['loses']
print(total)