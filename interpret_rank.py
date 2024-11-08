import json
import glob
import matplotlib.pyplot as plt

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def get_rank_matching(data, matching):
    for game in data:
        matching[int(abs(game['p1_rank'] - game['p2_rank']))] += 1

matching = [0]*30
games = glob.glob(f'data/rank/games_before_*.json')

for datas in games:
    data = load_data(datas)
    get_rank_matching(data, matching)
print(matching)

plt.figure(figsize=(10, 5))
plt.xticks(range(40))
plt.plot([i for i in range(30)], matching, marker='o', linestyle='', color='b')
plt.xlabel('+-rank')
plt.ylabel('games')
plt.title('games by +-rank')
plt.grid(True)
plt.show()