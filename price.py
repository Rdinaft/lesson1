def get_summ(one, two, delimiter = '&'): 
    #one = input('Enter first word: ')    
    #two = input('Enter second word: ')   
    end = one + ' ' + delimiter + ' ' + two
    end = str(end).upper()
    return end
print(get_summ('Learn', 'python'))

def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'
print(format_price(56.24))

