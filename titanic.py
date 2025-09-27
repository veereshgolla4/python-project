import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder 
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


df = pd.read_csv("titanic.csv")  

print("First 5 rows of dataset:")
print(df.head())
print("\nData info:")
print(df.info())




df = df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1)


imputer = SimpleImputer(strategy='median')
df['Age'] = imputer.fit_transform(df[['Age']])


df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])


le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])          
df['Embarked'] = le.fit_transform(df['Embarked'])


X = df.drop('Survived', axis=1)
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

plt.figure(figsize=(5,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


importances = model.feature_importances_
features = X.columns
plt.figure(figsize=(6,4))
sns.barplot(x=importances, y=features, palette="viridis")
plt.title("Feature Importance")
plt.show()
