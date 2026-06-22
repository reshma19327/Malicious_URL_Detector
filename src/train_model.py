import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import matplotlib.pyplot as plt
import seaborn as sns

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("dataset/malicious_phish.csv")

print("Dataset Loaded Successfully!")
print("Original Shape:", df.shape)

# ==========================
# Convert Labels
# benign = 0
# all others = 1
# ==========================

df["label"] = df["type"].apply(
    lambda x: 0 if x == "benign" else 1
)

# ==========================
# Use Sample Dataset
# ==========================

df = df.sample(
    n=20000,
    random_state=42
)

print("Sampled Shape:", df.shape)

# ==========================
# Feature Functions
# ==========================

def url_length(url):
    return len(str(url))

def count_dots(url):
    return str(url).count('.')

def count_digits(url):
    return sum(c.isdigit() for c in str(url))

def count_hyphens(url):
    return str(url).count('-')

def has_https(url):
    return 1 if str(url).startswith("https") else 0

def count_slashes(url):
    return str(url).count('/')

def count_question_marks(url):
    return str(url).count('?')

def count_equal_signs(url):
    return str(url).count('=')

def count_at_symbols(url):
    return str(url).count('@')

def count_underscores(url):
    return str(url).count('_')

# ==========================
# Feature Extraction
# ==========================

df["url_length"] = df["url"].apply(url_length)
df["dots"] = df["url"].apply(count_dots)
df["digits"] = df["url"].apply(count_digits)
df["hyphens"] = df["url"].apply(count_hyphens)
df["https"] = df["url"].apply(has_https)

df["slashes"] = df["url"].apply(count_slashes)
df["questions"] = df["url"].apply(count_question_marks)
df["equals"] = df["url"].apply(count_equal_signs)
df["ats"] = df["url"].apply(count_at_symbols)
df["underscores"] = df["url"].apply(count_underscores)

print("Features Extracted Successfully!")

# ==========================
# Features & Labels
# ==========================

X = df[
    [
        "url_length",
        "dots",
        "digits",
        "hyphens",
        "https",
        "slashes",
        "questions",
        "equals",
        "ats",
        "underscores"
    ]
]

y = df["label"]

# ==========================
# Train-Test Split
# ==========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# ==========================
# Train Model
# ==========================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("Model Trained Successfully!")

# ==========================
# Evaluation
# ==========================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ==========================
# Confusion Matrix
# ==========================

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 4))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()

# ==========================
# Test URL Prediction
# ==========================

test_url = "http://secure-bank-login-update.xyz"

test_df = pd.DataFrame(
    [[
        len(test_url),
        test_url.count('.'),
        sum(c.isdigit() for c in test_url),
        test_url.count('-'),
        1 if test_url.startswith("https") else 0,
        test_url.count('/'),
        test_url.count('?'),
        test_url.count('='),
        test_url.count('@'),
        test_url.count('_')
    ]],
    columns=[
        "url_length",
        "dots",
        "digits",
        "hyphens",
        "https",
        "slashes",
        "questions",
        "equals",
        "ats",
        "underscores"
    ]
)

prediction = model.predict(test_df)

if prediction[0] == 1:
    print("\nPrediction: Malicious URL")
else:
    print("\nPrediction: Safe URL")

# ==========================
# Save Model
# ==========================

joblib.dump(
    model,
    "models/url_detector.pkl"
)

print("\nModel saved successfully!")