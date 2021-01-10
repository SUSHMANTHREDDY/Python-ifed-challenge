import requests

def ability(name):
    url = 'https://pokeapi.co/api/v2/pokemon/' + name
    resp = requests.get(url=url)
    data = resp.json()
    answer = []
    for item in data['abilities']:
        answer.append((item['ability']['name']))
    return answer


if __name__ == '__main__':
    ability("machamp")