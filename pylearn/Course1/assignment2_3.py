# Get the hours and rate per hours 

hrs = input("Enter Hours: ")
hrs = float(hrs)
rate = input("Enter the rate per hour: ")
rate = float(rate)

# compute gross pay

pay = hrs * rate
pay = str(pay)

# Display the pay in required format

print('Pay: ' + pay)
