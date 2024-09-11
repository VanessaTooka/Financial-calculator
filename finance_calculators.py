import math

print("investment - to calculate the amount you'll have to pay on a home laon")
print("bond - to calculate the amount of interest uou'll earn on your investment")
print("Enter eithe 'investment' or 'bond' from the menu above to proceed:")

#Choose the transaction you want to do (loan or investments):
transaction=input("Select type of transation: ")
transaction.lower
    
if transaction == 'investment':
    principle = 0
    rate = 0
    time = 0 
   
#If the transaction selected is investment, calculate the total interest: 
#Choose the interst type (simple or compound)
 
    while principle <= 0:
        principle =float(input("Enter the principle amount, don't type any space: ")) 
    if principle <= 0:
        print('principle cannot be less than 0')

    while rate <= 0:
        rate =float(input('Enter the interest rate amount, no precentage sign: ')) 
    if rate <= 0:
        print('rate cannot be less than 0')      

    while time <= 0:
        time =int(input('Enter the time in years: ')) 
    if time <= 0:
        print('time cannot be less than 0')
    print(principle)
    print(rate)
    print(time)

#Select the desired inverest rate: 
    interest=(input('Select between simple interest and compound interest, type your selection in full: '))  
# 𝐴 = 𝑃(1 + 𝑟×𝑡)
#simple interest = principle * (1 + rate * time)
    simple_interest= principle * (1 + rate/100 * time)
    if interest== 'simple interest':
        print(f"R{simple_interest}")

#Compound interest = P * math.pow((1+r),t)
    compound_interest = principle * math.pow((1 + rate/100), time)
    if interest == 'compound interest':
        print(f"R{compound_interest:.2f}")

#Calculate home bond transation:      
if transaction == 'bond':
    present_value = 0
    interest_rate= 0
    number_of_months = 0 

    while present_value <= 0:
        present_value =float(input("Enter the present value amount, don't type any space: ")) 
    if present_value <= 0:
        print('present value cannot be less than 0')

    while interest_rate <= 0:
        interest_rate=float(input('Enter the monthly interest amount: '))
    if interest_rate <= 0:
        print('rate cannot be less than 0')      

    while number_of_months <= 0:
        number_of_months =float(input('Enter the number of months: ')) 
    if number_of_months <= 0:
        print('number of months cannot be less than 0')

#repayment = (i * P)/(1 - (1 + i)**(-n))
    monthly_interest=((interest_rate/100)/12)  
    repayment=(f"{(monthly_interest * present_value)/(1-(1 + monthly_interest)**(-number_of_months)):.2f}")
    print(repayment)
    print(f"R{repayment}")
    
else: transaction== ""
print('error')