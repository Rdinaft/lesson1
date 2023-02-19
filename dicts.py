hero_name = input('Enter your name:')

stats = [
    {
    'name': hero_name, 
    'strengh': 10, 
    'agility': 15, 
    'intelligence': 2,
    'talents': ['Shield bash', 'Heroic strike'],
    },
    
    {'name': 'slime', 'attack': 2, 'health': 10},
    
    {'name': 'wolf', 'attack': 5, 'health': 14},
] 
stats[0]['talents'].append('Stun')
stats[1]['health'] = stats[1]['health'] - 2
print(stats)

weather_report = {'city': 'Moscow', 'temperature': '20'}
print(weather_report['city'])
weather_report['temperature'] = int(weather_report['temperature']) - 5
print(weather_report)

print(weather_report.get('country'))
print(weather_report.get('country', 'Russia'))
weather_report['date'] = '27.05.2019'
print(len(weather_report))