# Malicious URL Detection Using Machine Learning

## Project Overview

The Malicious URL Detection System is a Machine Learning-based web application that identifies whether a given URL is safe or malicious.

The system analyzes URL characteristics such as length, number of dots, digits, hyphens, special characters, and HTTPS usage to classify URLs using a Random Forest Classifier.

The project helps users detect potentially dangerous websites and phishing links before accessing them.

---

## Features

* Detects Safe and Malicious URLs
* Machine Learning-based Classification
* Random Forest Algorithm
* Feature Engineering on URLs
* Confusion Matrix Visualization
* Flask Web Application Interface
* Real-time URL Prediction
* Model Persistence using Joblib

---

## Dataset

Dataset: Malicious URLs Dataset

Total Records: 651,191 URLs

Classes:

* Benign
* Phishing
* Malware
* Defacement

For binary classification:

* Safe (0) = Benign
* Malicious (1) = Phishing, Malware, Defacement

---

## Technologies Used

* Python
* Pandas
* Scikit-Learn
* Flask
* Matplotlib
* Seaborn
* Joblib
* HTML
* Git & GitHub

---

## Machine Learning Model

Algorithm Used:

* Random Forest Classifier

Features Extracted:

* URL Length
* Number of Dots
* Number of Digits
* Number of Hyphens
* HTTPS Presence
* Number of Slashes
* Number of Question Marks
* Number of Equal Signs
* Number of @ Symbols
* Number of Underscores

---

## Model Performance

Accuracy: 88.02%

Classification Results:

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 88.02% |
| Precision | 82%    |
| Recall    | 82%    |
| F1-Score  | 82%    |

---

## Project Structure

```text
Malicious_URL_Detector
│
├── app.py
├── requirements.txt
├── README.md
│
├── dataset
│   └── malicious_phish.csv
│
├── models
│   └── url_detector.pkl
│
├── src
│   ├── feature_extraction.py
│   └── train_model.py
│
├── templates
│   └── index.html
│
└── venv
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/reshma19327/Malicious_URL_Detector.git
```

Navigate to the project:

```bash
cd Malicious_URL_Detector
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

Train the model:

```bash
python src/train_model.py
```

Run the Flask application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Future Enhancements

* Improve accuracy using advanced feature engineering
* Add domain reputation analysis
* Integrate deep learning models
* Deploy application on cloud platforms
* Add prediction confidence score
* Create browser extension for real-time protection

---

## Author

Reshma Ajesh

Computer Science and Artificial Intelligence Student

Machine Learning | Deep Learning | Cybersecurity | Cloud Computing

