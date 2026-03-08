# simple Navie Bayes using Email Filter

#prior probabilites
P_spam = 0.4
P_not_spam = 0.6

# Likelihoods
P_offer_given_spam = 0.8
P_offer_given_not_spam = 0.2

# total probability
P_offer = (P_offer_given_spam * P_spam) + \
            (P_offer_given_not_spam*P_not_spam)

# Posterior
P_spam_given_offer = (P_offer_given_spam * P_spam) / P_offer

print("Probability email is spam: ",P_spam_given_offer)

if P_spam_given_offer > 0.5:
    print("Classified as SPAM")
else:
    print("Classified as NOT SPAM")
    