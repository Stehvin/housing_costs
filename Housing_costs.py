# -*- coding: utf-8 -*-

Loan = 75000
DownPayment = 15000
AnnualInterestRate = 0.035
StockMarketRate = 0.06
LoanLength = 120
CurrentTimeYears = 1

def FixedMonthlyPayment(UnpaidLoanAmount, AnnualInterestRate, Months):
    MonthlyRate = AnnualInterestRate/12    
    numerator = UnpaidLoanAmount * MonthlyRate * ((1 + MonthlyRate)**Months)
    denomenator = ((1 + MonthlyRate)**Months) - 1
    return numerator/denomenator

def RemainingBalance(UnpaidLoanAmount, AnnualInterestRate, Months, MonthsPaid):
    MonthlyRate = AnnualInterestRate/12    
    numerator = UnpaidLoanAmount * (((1 + MonthlyRate)**Months) - \
                ((1 + MonthlyRate)**MonthsPaid))
    denomenator = ((1 + MonthlyRate)**Months) - 1
    return numerator/denomenator
    
def OpportunityCost(DownPayment, fixed_monthly_payment, StockMarketRate,
                    CurrentTimeYears): 
    balance = 0    
    YearNet = (800 - fixed_monthly_payment) * 12   
    for i in range(CurrentTimeYears):
        balance = (balance + YearNet)*(1+StockMarketRate)
    Total_Cost = ((DownPayment*((1+StockMarketRate)**CurrentTimeYears)) * \
                    -1) + balance
    return Total_Cost

MonthlyPay = FixedMonthlyPayment(Loan - DownPayment, AnnualInterestRate, 
                                 LoanLength)
LeftToPay = RemainingBalance(Loan - DownPayment, AnnualInterestRate, LoanLength,
                             CurrentTimeYears*12)
OppCost = OpportunityCost(DownPayment, MonthlyPay, StockMarketRate, CurrentTimeYears)
print('Monthly Payment: ' + str(MonthlyPay))
print('RemainingBalance: ' + str(LeftToPay))
print('Opportunity Costs (Assuming $800 rent): ' + str(OppCost))
                                              
print('Net Gain/Loss: ' + str((Loan*.85) - LeftToPay + OppCost))