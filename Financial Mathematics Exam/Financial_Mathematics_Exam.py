# Interest calculation
principal_amount = float(input("Principal amount: "))
int_rate = float(input("effective Annual Interest Rate: "))
period = float(input("Number of periods: "))

def FV_value(amount, rate, year):
    value = (amount * (1+rate))**year
    return value

print(FV_value(principal_amount, int_rate,period))

# Customer Inputs
principal_amount = float(input("Principal amount: "))
int_rate = float(input("effective Annual Interest Rate: "))
period = float(input("Number of periods: "))

# Annuity Immediate
def PV_annuity_imm(amount, rate, year):
    factor = 1/((1+rate)**year)
    value = amount*((1-factor)/rate)
    return value

# Annuity Due
def PV_annuity_due(rate):
    val = PV_annuity_imm(principal_amount, int_rate, period)
    factor = (1+rate)
    return round(val*(1+rate))

print(PV_annuity_due(int_rate))

# Net Present Value with a constant cash flow
user_CF = float(input("Constant cash flow per period: "))
user_rate = float(input("Interest rate per period"))
user_time = float(input("Number of periods: "))

def NPV(CF, rate, year):
    sum = 0
    for i in range(1,year+1):
        cash_flow = CF/((1+rate)**i)
        sum = sum + cash_flow
    return sum

print(NPV(user_CF,user_rate,user_time))

# Oustanding Loan Balance - Retrospective method
def Loan_bal(outstanding_bal, rate, periods, repayment):
    val1 = outstanding_bal*((1+rate)**periods)
    factor = (((1+rate)**periods) - 1)/rate
    return (val1 - repayment*factor)
print(Loan_bal(1000,0.05,11,90))

# Bond Pricing
F = 1000
C = 1300
r = 0.05
i = 0.04
n = 10

def bondprice(faceval, c_rate, redemp_val, y_rate, no_pmt):
    factor = (1/(1+y_rate))**no_pmt
    return faceval * c_rate * ((1-factor)/y_rate) + redemp_val*factor

def classification(F,P,C,r,i):
    if (P == C) | (F*r == C*i):
        return "Bond is a par value bond"
    elif (P > C) | (F*r > C*i):
        return "Bond is a premium bond"
    elif (P < C) | (F*r < C*i):
        return "Bond is a discount bond"

P = bondprice(F,r,C,i,n)
print(classification(F,P,C,r,i))