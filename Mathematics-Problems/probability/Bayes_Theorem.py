"""
2% people have a disease.

Test accuracy:

If disease → 95% positive

If no disease → 10% false positive

Find probability person has disease given positive test.
"""

P_D = 0.02
P_T_given_D  = 0.95
P_T_given_notD = 0.10
P_not_D = 1 - P_D

P_T = P_T_given_D * P_D + P_T_given_notD * P_not_D
P_D_given_T = (P_T_given_D * P_D) / P_T

print("Probability of disease given position test: ",(P_D_given_T)*100)
