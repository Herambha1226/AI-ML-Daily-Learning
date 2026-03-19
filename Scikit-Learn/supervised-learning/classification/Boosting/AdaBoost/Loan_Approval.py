# import necessary modules
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd 
import matplotlib.pyplot as plt 
import warnings
warnings.filterwarnings('ignore')

data = {
    "age": [25,30,45,35,22,40,50,23,37,29],
    "income": [20000,30000,50000,40000,15000,60000,70000,18000,45000,32000],
    "credit_score": [600,650,700,680,550,720,750,580,690,660],
    "loan_amount": [100000,150000,200000,180000,90000,220000,250000,120000,170000,140000],
    "past_default": [0,0,1,0,1,0,0,1,0,0],
    "approved": [0,1,1,1,0,1,1,0,1,1]
}

df = pd.DataFrame(data)

print("Loan Approval Data : \n",df)

x = df.drop('approved',axis=1)
y = df["approved"]

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.3,random_state=42,stratify=y
)

weak_model = DecisionTreeClassifier(max_depth=1)

model = AdaBoostClassifier(estimator=weak_model,n_estimators=100,learning_rate=0.2)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print("Accuracy Score : ",accuracy_score(y_test,y_pred))
print("Confuion Matrix: \n",confusion_matrix(y_test,y_pred))

color = ['red' if val == 0 else 'green' for val in df['approved']]

plt.scatter(df["credit_score"],df["approved"],c=color)
plt.title("Loan Approve Based On Credit Score")
plt.xlabel("Credit Score")
plt.ylabel("Approved")
plt.show()