"""
Propositional Logic (Basics)
📐 Math idea

Statements are either True or False.

Operations:

AND (∧)

OR (∨)

NOT (¬)
"""

age = 22
income = 30000

print(age > 18 and income > 20000)
print(age > 18 or income > 50000)
print(not age > 18)

# 2️⃣ If–Else = Logical Rule
def loan_approval(score):
    if score > 700:
        return "Approved"
    else:
        return "Rejected"
print(loan_approval(750))


# 3️⃣ Combining Multiple Conditions
def approve(age,salary,credit):
    if (age > 21 and salary > 25000) or credit > 750:
        return "Approve"
    return "Rejected"
print(approve(20,20000,780))

values = [True,False]
for p in values:
    for q in values:
        print(p, q, p and q)

# 5️⃣ Predicate Logic (Logic with variables)
ages = [19,22,30,40,20]

print(all(age > 18 for age in ages))
print(any(age < 18 for age in ages))


