names = ['Michael', 'Sarah', 'John']
print(names)

#names.append('Nick')
#print(names)

#print(names.count('Michael'))

#print(len(names))

#print(names[3])

#print('Nick' in names)

del names[1]
print(names)

names.remove('John')
print(names)

numbers = [3, 5, 7, '9', 10.5] #для числовых значений кавычки не нужны?
print(numbers)
numbers.append('Python')
print(len(numbers))

print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
numbers.remove('Python')