import random

x = random.randint(0, 6)
y = 6

z = y - x

def death_roulette(num):
    if z == 0:
        print('Death!')
    else:
        print('Alive!')
death_roulette(z)