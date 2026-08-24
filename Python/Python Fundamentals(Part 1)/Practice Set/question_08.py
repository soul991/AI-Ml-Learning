'''Q9.
Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float 
and compute simple interest:
SI= (P * R * T )/100'''

P = int(input("Enter the Principal: "))
R = int(input("Enter the interest rate: "))
T = int(input("Enter the time period: "))

I = ((P*R*T)/100)
TA = P + I #TA = Total Returning Amount(Interest + Principal)
print("The interest is", I)
print("Total returning amount", TA)