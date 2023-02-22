gross_income = int( input("what is your gross income"))
tax_group_A =(gross_income *0.05)
tax_group_B =(gross_income *0.10)
tax_group_C =(gross_income *0.15)
tax_group_D =(gross_income *0.20)

if gross_income < 100000:
    print("Gross income:",gross_income)
    print("net income:" ,gross_income - tax_group_A)
elif(gross_income > 100000) & (gross_income <150000):
    print("Gross_income:",gross_income) 
    print("Net_income:",gross_income - tax_group_B) 
elif(gross_income >=150000) & (gross_income <= 300000):
    print("Gross_income:" ,gross_income)
    print("Net_income:", gross_income - tax_group_C)
else:
    print("Gross_income:", gross_income)
    print("Net_income:", gross_income - tax_group_D )
