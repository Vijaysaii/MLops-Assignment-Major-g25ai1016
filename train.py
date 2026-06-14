import joblib
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data = fetch_olivetti_faces(shuffle=True, random_state=42)
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=42
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

joblib.dump((model, X_test, y_test), "savedmodel.pth")
print(f"Model trained on {len(X_train)} samples and saved to savedmodel.pth")
