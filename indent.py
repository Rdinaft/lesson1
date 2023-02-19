import random

damage = random.randint(0, 6)
start_health = 6

result_health = start_health - damage

def death_roulette(num):
    if result_health == 0:
        print('Death!')
    else:
        print('Alive!')
death_roulette(result_health)