#price = 100
#discount = 5

#price_with_discount = price - price * discount / 100

#print(price_with_discount)

def get_summ(one, two, delimiter = '&'): 
    #one = input('Enter first word: ')    
    #two = input('Enter second word: ')   
    end = one + ' ' + delimiter + ' ' + two
    end = str(end).upper()
    print(end)
get_summ('Learn', 'python')

def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'
print(format_price(56.24))

