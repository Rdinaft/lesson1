def get_summ(one, two, delimiter = '&'):   
   
    end = one + ' ' + delimiter + ' ' + two
    end = str(end).upper()
    return end

def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'


if __name__ == '__main__':
    print(get_summ('Learn', 'python'))
    print(format_price(56.24))