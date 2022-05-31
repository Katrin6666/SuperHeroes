from pprint import pprint
import requests

def get_character():
    heroes_list = ['Hulk', 'Captain america', 'Thanos']
    intelligences = {'Hulk': 0, 'Captain america': 0, 'Thanos': 0}
    the_best_intelligence = 0
    the_best_hero = 0
    for hero in heroes_list:
        url = f"https://superheroapi.com/api/2619421814940190/search/{hero}"
        resp = requests.get(url).json()
        intellect = resp['results'][0]['powerstats']
        intelligences[hero] = intellect['intelligence']
        if int(intellect['intelligence']) > the_best_intelligence:
            the_best_intelligence = int(intellect['intelligence'])
            the_best_hero = hero
    print(intelligences)
    print(f'Самый умный {hero}, его IQ = {the_best_intelligence}')

if __name__ == '__main__':
    get_character()

