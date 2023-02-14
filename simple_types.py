a = ('HelloU').capitalize().replace('u','')
print(a)

a = 2
b = 0.5
print(a + b)

name = input('Введите ваше имя: ')
print(f'Привет, {name}! Как оно?')

v = input('Введите число от 1 до 10: ')
print(float(v) + 10) 

print(float('1'))  # 1
#print(int('2.5'))  # ValueError
print(bool(1))  # True
print(bool(''))  # False
print(bool(0))  # False