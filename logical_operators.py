# ------------- Logical Operators -------------

"""
1- AND
2- OR
3- NOT
"""
# Example 1 ->>> AND
high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")

# Example 2 ->>> OR
high_income1 = True
good_credit1 = False

if high_income1 or good_credit:
    print("Eligible for Loan")
else:
    print("Not Eligible for Loan")
