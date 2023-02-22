import random


def death_roulette():
    damage = random.randint(0, 6)
    start_health = 6

    result_health = start_health - damage

    if result_health == 0:
        print('Death!')
    else:
        print('Alive!')

        
if __name__ == '__main__':
    death_roulette()