import requests
import random
import json
import time
from rich.progress import Progress

wordlist_datei = 'diceware-dereko.txt'
useragents_datei = 'useragents.json'

with open(useragents_datei, 'r', encoding='utf-8') as file:
    user_agents_data = json.load(file)
    user_agents = [entry['ua'] for entry in user_agents_data]

with open(wordlist_datei, 'r', encoding='utf-8') as file:
    wordlist = [line.split('\t')[1] for line in file.read().splitlines()]

def random_search():
    iteration = 1
    while True:
        print(f"\n[INFO] Iteration {iteration}")
        iteration += 1
        word = random.choice(wordlist)
        search = f"{word}"
        print(f"[INFO] Searchterm: \"{search}\"")
        searchengine = random.choice(['google', 'wikipedia'])
        if searchengine == 'google':
            url = f"https://www.google.com/search?q={search}"
        else:
            url = f"https://en.wikipedia.org/wiki/{search.replace(' ', '_')}"
        user_agent = random.choice(user_agents)
        headers = {
            'User-Agent': user_agent
        }
        try:
            response = requests.get(url, headers=headers, verify=True)
            if response.status_code == 200:
                print(f"[SUCCESS] Request to {searchengine}")
            elif response.status_code == 404:
                print(f"[ERROR] Request to {searchengine} 404")
            else:
                print(f"[ERROR] Request to {searchengine} {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Request to {searchengine} fail: {e}")

        wait = random.randint(1 * 60, 30 * 60)
        print(f"[INFO] Wait {wait // 60} min {wait % 60} sec for next search")

        with Progress() as progress:
            task = progress.add_task("[cyan]Wait...", total=wait)
            for _ in range(wait):
                time.sleep(1)
                progress.update(task, advance=1)

if __name__ == "__main__":
    random_search()
