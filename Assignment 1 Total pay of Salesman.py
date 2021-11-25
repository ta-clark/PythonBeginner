# Weekly pay for a salesman

hours_worked = eval(input("Enter Hours Worked: "))
# Ask user for hours worked

weekly_sales = eval(input("Enter Number of Weekly Sales: "))
# Ask user for number of weekly sales

commission = weekly_sales * .30
# Commission is set at 20% of weekly sales

hourly_rate = 35
# Hourly rate is set at $35/hr

total_pay = hours_worked * hourly_rate + commission
print(total_pay)
# Total amount paid is based on the hourly rate x hours worked + commission
