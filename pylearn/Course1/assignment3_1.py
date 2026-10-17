hrs = input('Enter hours worked: ')
try :
    h = float(hrs)
except:
    h = 0.0
    print('Since we did not get a number, we assume hours worked was 0')
rate = input('Enter rate per hour: ')
try :
    r = float(rate)
except:
    r = 1.0
    print('Since we did not get a number, we assume rate was 1')
if (h<=40) :
    pay = h * r
else :
    pay = (40 * r) + ((h-40) * (r * 1.5))
print (pay)
