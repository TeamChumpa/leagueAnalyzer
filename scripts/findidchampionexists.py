import os
import requests

summoner_id = input('Enter the summoner id: ')
print('Enter the range of champion id')
start_champion_id = input('From: ')
end_champion_id = input('To: ')

result = {}

for champion_id in range(int(start_champion_id), int(end_champion_id) + 1):
    URL = 'https://ru.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{}/by-champion/{}?api_key={}'.format(
        summoner_id, champion_id, os.getenv('LOL_API_KEY'))
    data = requests.get(url=URL)
    if data.status_code is 200:
        result[champion_id] = data.json()['championPoints']

print(result)