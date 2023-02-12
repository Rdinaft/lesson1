#from pprint import pprint

hero_name = input('Enter your name:')
stats = [
    {'name': hero_name, 
    'strengh': 10, 
    'agility': 15, 
    'intelligence': 2,
    'talents': ['Shield bash', 'Heroic strike']},
    {'name': 'slime', 'attack': 2, 'health': 10},
    {'name': 'wolf', 'attack': 5, 'health': 14}
] 
#default_name = 'Anon'
#print(stats)
stats[0]['talents'].append('Stun')
stats[1]['health'] = stats[1]['health'] - 2
print(stats)
#print(stats.get('name', default_name))