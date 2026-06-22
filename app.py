from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("models/url_detector.pkl")

def extract_features(url):
    return pd.DataFrame([{
        "url_length": len(url),
        "dots": url.count('.'),
        "digits": sum(c.isdigit() for c in url),
        "hyphens": url.count('-'),
        "https": 1 if url.startswith("https") else 0,
        "slashes": url.count('/'),
        "questions": url.count('?'),
        "equals": url.count('='),
        "ats": url.count('@'),
        "underscores": url.count('_')
    }])

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        url = request.form["url"]

        features = extract_features(url)

        result = model.predict(features)[0]

        if result == 1:
            prediction = "⚠️ Malicious URL"
        else:
            prediction = "✅ Safe URL"

    return render_template(
        "index.html",
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)