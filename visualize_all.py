import json
import matplotlib.pyplot as plt

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

data = load_data('data/replays.json')["rates"]

chara_ids = [data.index(item) for item in data]
winrates = [item["winrate"] for item in data]

plt.figure(figsize=(10, 5))
plt.xticks(range(40))
plt.plot(chara_ids, winrates, marker='o', linestyle='', color='b')
plt.xlabel('Character ID')
plt.ylabel('Winrate')
plt.title('Winrate by Chara ID')
plt.grid(True)
plt.show()  

chara_ids = [data.index(item) for item in data]
winrates = [item["wins"]+item["loses"] for item in data]

plt.figure(figsize=(10, 5))
plt.xticks(range(40))
plt.plot(chara_ids, winrates, marker='o', linestyle='', color='b')
plt.xlabel('Character ID')
plt.ylabel('Games')
plt.title('Games by Chara ID')
plt.grid(True)
plt.show()  