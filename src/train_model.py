import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
df = pd.read_csv("dataset.csv")

# -------------------------
# Feature Extraction Functions
# -------------------------

def url_length(url):
    return len(url)

def count_dots(url):
    return url.count('.')

def count_digits(url):
    return sum(c.isdigit() for c in url)

def count_hyphens(url):
    return url.count('-')

def has_https(url):
    return 1 if url.startswith("https") else 0

# -------------------------
# Generate Features
# -------------------------

df["url_length"] = df["url"].apply(url_length)
df["dots"] = df["url"].apply(count_dots)
df["digits"] = df["url"].apply(count_digits)
df["hyphens"] = df["url"].apply(count_hyphens)
df["https"] = df["url"].apply(has_https)

# Features and Labels

X = df[["url_length", "dots", "digits", "hyphens", "https"]]
y = df["label"]

# -------------------------
# Train Model
# -------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

print("Model trained successfully!")

# -------------------------
# Test Prediction
# -------------------------

test_url = "http://secure-bank-login-update.xyz"

test_df = pd.DataFrame(
    [[
        len(test_url),
        test_url.count('.'),
        sum(c.isdigit() for c in test_url),
        test_url.count('-'),
        1 if test_url.startswith("https") else 0
    ]],
    columns=["url_length", "dots", "digits", "hyphens", "https"]
)

prediction = model.predict(test_df)

if prediction[0] == 1:
    print("Prediction: Malicious URL")
else:
    print("Prediction: Safe URL")

# -------------------------
# Save Model
# -------------------------

joblib.dump(model, "models/url_detector.pkl")

print("Model saved successfully!")