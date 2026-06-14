import joblib
from sklearn.metrics import accuracy_score

model, X_test, y_test = joblib.load("savedmodel.pth")
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy: {accuracy * 100:.2f}%")
