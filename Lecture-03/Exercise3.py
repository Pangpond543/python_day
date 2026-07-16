hours_worked = int(input("Enter your number of hours worked: "))
pay_rate = int(input("Enter your pay rate: "))
if hours_worked > 40:
    ot =(hours_worked - 40)
    hours_worked = (hours_worked - ot)
    ot = ((ot * pay_rate) * 1.5)
    
gross_pay = hours_worked * pay_rate + ot

print("The gross pay is: $", gross_pay)