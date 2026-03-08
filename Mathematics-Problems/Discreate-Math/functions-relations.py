"""What is a Function (core ML idea)
📐 Math idea

A function maps each input to exactly one output."""

# Convert input → class/category
def classify(score):
    if score >= 50:
        return "Pass"
    else: 
        return "Fail"
print(classify(80))
print(classify(30))

"""
Relation → Function (VERY IMPORTANT)
📐 Math

Relation becomes function if each input has only one output.

"""
dataset = {
    "email1" : "spam",
    "email2" : "not_spam",
    "email3" : "spam"
}

def model(x):
    return dataset[x]

print(model("email3"))


"""
Function Composition (Pipeline!)
📐 Math
(f ∘ g)(x) = f(g(x))
"""

def normalize(x):
    return x / 100

def predict(x):
    return "High" if x > 0.5 else "Low"

print(predict(normalize(90)))

# Real ML-style Tiny Example
def extract_features(text):
    return len(text)
def spam_classifier(lenght):
    return "spam" if lenght > 20 else "not spam"
email = "Win money now!!!"
features = extract_features(email)
print(spam_classifier(features))
