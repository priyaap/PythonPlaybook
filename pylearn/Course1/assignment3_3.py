score = input('Enter Score: ')
try:
    score = float(score)
    if (score < 0.0 or score > 1.0) :
        print('Score can only be numeric and between 0.0 to 1.0')
    elif (score<0.6) :
        print('F')
    elif(score<0.7) :
        print('D')
    elif(score<0.8) :
        print('C')
    elif(score<0.9) :
        print('B')
    elif(score<=1.0) :
        print('A')    
except:
    print('Score can only be numeric and between 0.0 to 1.0')