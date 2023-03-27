
def payMinMonthly(balance,annualInterestRate,minMonthlyPaymentRate):
    '''   
    Parameters
    ----------
    balance : credit card balance,float.
    annualInterestRate : float between 0 and 1
    minMonthlyPaymentRate : float between 0 and 1

    Returns
    -------
    balance : balance amount after paying only min payment each month

    '''
    for i in range(12):
        minMonthlyPayment=round(minMonthlyPaymentRate*balance,2)
        unpaidMonthlyBal=balance-minMonthlyPayment
        updatedBalance=round(unpaidMonthlyBal + (unpaidMonthlyBal*(annualInterestRate/12)),2)
        balance=updatedBalance
    return balance
    
    
#print(payMinMonthly(42,0.2,0.04))

def payFixedMonthly(balance,annualInterestRate,minFixed):
    '''
    Parameters
    ----------
    balance : credit card balance,float
    annualInterestRate : float between 0 and 1
    minFixed : num

    Returns
    -------
    balance : balance amount after paying fixed payment each month
    '''
    for i in range(12):
        monthlyRate=annualInterestRate/12
        unpaidMonthlyBal=balance-minFixed
        updatedBalance=round(unpaidMonthlyBal + (unpaidMonthlyBal*monthlyRate),2)
        balance=updatedBalance
    return balance
             
        
def pay12Months(balance,annualInterestRate,minFixed):
    '''
    Parameters
    ----------
    balance : credit card balance,float.
    annualInterestRate : float between 0 and 1
    minFixed : multiples of 10

    Returns
    -------
    minFixed = Min amount need to be paid to clear the debt in a year as multiples of 10.

    '''
    if payFixedMonthly(balance,annualInterestRate,minFixed)<=0:
        return minFixed
    else:
        return pay12Months(balance, annualInterestRate,minFixed+10)


def pay12MonthsBisection(balance, annualInterestRate):
    monthlyRate=annualInterestRate/12
    monthlyLower = balance/12
    monthlyUpper = balance*((1+monthlyRate)**12)/12
    return monthlyLower, monthlyUpper

def exactAmount(balance,annualInterestRate,monthlyLower, monthlyUpper):
    monthlyBisect = (monthlyLower+monthlyUpper)/2
    balance_val=payFixedMonthly(balance,annualInterestRate,monthlyBisect)
    if balance_val==0:
        return round(monthlyBisect,2)
    elif balance_val<0:       
        monthlyUpper = monthlyBisect
        return exactAmount(balance,annualInterestRate, monthlyLower, monthlyUpper)
    else: 
        monthlyLower = monthlyBisect
        return exactAmount(balance,annualInterestRate, monthlyLower, monthlyUpper)

balance=999999
annualInterestRate=0.18
monthlyLower, monthlyUpper=pay12MonthsBisection(balance, annualInterestRate)      
print(exactAmount(balance, annualInterestRate,monthlyLower, monthlyUpper))

    
    
    
    
    
    
    
    