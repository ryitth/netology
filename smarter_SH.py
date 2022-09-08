import requests

url = requests.get('https://akabab.github.io/superhero-api/api/glossary.html')

cap = url.text.find('<td>Captain America</td>')
hulk = url.text.find('<td>Hulk</td>')
thanos = url.text.find('<td>Thanos</td>')

with open('super.txt', 'w') as f:
    f.write(url.text)


int_cap = int(url.text[cap + len('<td>Captain America</td>') + 11: cap + 37])
int_hulk = int(url.text[hulk + len('<td>Hulk</td>') + 11: hulk + 26])
int_thanos = int(url.text[thanos + len('<td>Thanos</td>') + 11: thanos + 29])

n = [('Thanos', int_thanos), ('Hulk', int_hulk), ('Captain America', int_cap)]

n.sort(key=lambda x: x[1])

print(f'Умнее всех из этих троих {n[-1][0]}')

