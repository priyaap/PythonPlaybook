#write a program which repeatedly reads numbers until user enters "done"
#Once done is entered, print total, count and avg
#if user enters anyting other than number detect their mistake using try and except

count = 0
tot = 0.0

while True :
    num = input('Enter your number here: ')
    if num == 'done' :
        break
    try :
        num = float(num)
    except :
        input('Invalid data. Enter a number or enter done...')
        continue
    count = count + 1
    tot = tot + num
print(count,tot,tot/count)












"""
#Original Solution

n = None
sum = 0
avg = 0
count = 0
while n != "done" :
    n = input ("Enter your next number here: ")
    try :
        n = int(n)
        sum = sum + n
        count = count + 1
    except :
        if n!= "done" : 
            print("Enter only numeric values")
avg = sum / count
print("Sum of the numbers you entered = ", sum)
print("Count of the numbers you entered = ", count)
print("Average of the numbers you entered = ", avg)

"""