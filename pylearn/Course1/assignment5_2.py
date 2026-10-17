max = None
min = None

while True :
    num = input('Enter your integer number here: ')
    if num == 'done' :
        break
    try :
        num = int(num)
    except :
        print('Invalid Data')
        continue
    if max is None :
        max = num
    elif num > max :
            max = num
    if min is None :
        min = num
    elif num < min :
        min = num
    
if max == None :
    print('No numbers entered')
else :
    print('Maximum is ', max)
    print('Minimum is ', min)
    
