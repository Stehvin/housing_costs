# -*- coding: utf-8 -*-

# input parameters
Loan = 200000
DownPayment = 40000
AnnualInterestRate = 0.035
LoanLength = 20             # length of loan in years
CurrentTimeYears = 10       # current time in years
HouseSellValue = 0.85
RentPrice = 1000
StockMarketRate = 0.06

def main():
    MonthlyPay = FixedMonthlyPayment(Loan - DownPayment, AnnualInterestRate, 
                                     LoanLength*12)
    LeftToPay = RemainingBalance(Loan - DownPayment, AnnualInterestRate, 
                                 LoanLength*12, CurrentTimeYears*12)
    OppCost = OpportunityCost(DownPayment, MonthlyPay, StockMarketRate, 
                              CurrentTimeYears, RentPrice)
    print('Monthly Payment: ' + '{:.2f}'.format(MonthlyPay))
    print('Remaining Balance: ' + '{:.2f}'.format(LeftToPay))
    print('Opportunity Costs (Assuming $' + str(RentPrice) + ' rent): ' + 
          '{:.2f}'.format(OppCost))
    print('Net Gain/Loss: ' + '{:.2f}'.format((Loan*HouseSellValue) - 
                                               LeftToPay + OppCost))

def FixedMonthlyPayment(UnpaidLoanAmount, AnnualInterestRate, Months):
    """Calculate the fixed monthly loan payment.
    Formula: P = L[c(1 + c)n]/[(1 + c)n - 1]
    Where P = monthly payment, L = original loan amount, 
    n = loan length in months, and c = monthly interest rate.
    """
    MonthlyRate = AnnualInterestRate/12    
    numerator = UnpaidLoanAmount * MonthlyRate * ((1 + MonthlyRate)**Months)
    denomenator = ((1 + MonthlyRate)**Months) - 1
    return numerator/denomenator

def RemainingBalance(UnpaidLoanAmount, AnnualInterestRate, Months, 
                     MonthsPaid):
    """Calculate the remaining loan balance.
    Formula: B = L[(1 + c)n - (1 + c)p]/[(1 + c)n - 1]
    Where B = remaining balance, L = original loan amount, 
    n = loan length in months, p = months passed, 
    and c = monthly interest rate.
    """
    MonthlyRate = AnnualInterestRate/12    
    numerator = UnpaidLoanAmount * (((1 + MonthlyRate)**Months) - \
                ((1 + MonthlyRate)**MonthsPaid))
    denomenator = ((1 + MonthlyRate)**Months) - 1
    return numerator/denomenator
    
def OpportunityCost(DownPayment, fixed_monthly_payment, StockMarketRate,
                    CurrentTimeYears, RentPrice): 
    """Calculate the opportunity cost of investment revenue and monthly 
    housing expense compared to renting.
    """
    balance = 0
    
    # monthly housing expense compared to renting,
    # could be positive or negative
    YearNet = (RentPrice - fixed_monthly_payment) * 12
    
    # renting vs buying opportunity gain/cost
    for i in range(CurrentTimeYears):
        balance = (balance + YearNet)*(1+StockMarketRate)
    
    # total opporunity cost includes down payment opportunity cost
    Total_Cost = ((DownPayment*((1+StockMarketRate)**CurrentTimeYears)) * \
                    -1) + balance
    return Total_Cost

if __name__ == "__main__":
    main()