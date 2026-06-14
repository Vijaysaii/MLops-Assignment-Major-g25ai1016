import io
import joblib
import numpy as np
from flask import Flask, render_template_string, request
from PIL import Image

app = Flask(__name__)

model, _, _ = joblib.load("savedmodel.pth")

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Olivetti Face Classifier</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 600px; margin: 60px auto; padding: 20px; }
    h1 { color: #333; }
    .result { margin-top: 20px; padding: 16px; background: #f0f4ff; border-radius: 8px; font-size: 1.2rem; }
    .error  { margin-top: 20px; padding: 16px; background: #fff0f0; border-radius: 8px; color: #c00; }
    input[type=file] { margin: 12px 0; }
    button { background: #4a6cf7; color: #fff; border: none; padding: 10px 24px; border-radius: 6px; cursor: pointer; font-size: 1rem; }
    button:hover { background: #3a5ce7; }
  </style>
</head>
<body>
  <h1>Olivetti Face Classifier</h1>
  <p>Upload a <strong>64×64 grayscale</strong> face image to predict its subject ID (0–39).</p>
  <form method="POST" enctype="multipart/form-data">
    <input type="file" name="image" accept="image/*" required />
    <br/>
    <button type="submit">Predict</button>
  </form>
  {% if prediction is not none %}
    <div class="result">Predicted Subject ID: <strong>{{ prediction }}</strong></div>
  {% endif %}
  {% if error %}
    <div class="error">{{ error }}</div>
  {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None
    if request.method == "POST":
        file = request.files.get("image")
        if not file or file.filename == "":
            error = "No file selected."
        else:
            try:
                img = Image.open(io.BytesIO(file.read())).convert("L").resize((64, 64))
                features = np.array(img).flatten().reshape(1, -1) / 255.0
                prediction = int(model.predict(features)[0])
            except Exception as exc:
                error = f"Prediction failed: {exc}"
    return render_template_string(HTML, prediction=prediction, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
