import pandas as pd

# Load dataset
df = pd.read_csv("dataset.csv")

# Feature 1: URL Length
def url_length(url):
    return len(url)

# Feature 2: Number of dots
def count_dots(url):
    return url.count('.')

# Feature 3: Number of digits
def count_digits(url):
    return sum(c.isdigit() for c in url)

# Feature 4: Number of hyphens
def count_hyphens(url):
    return url.count('-')

# Feature 5: HTTPS present
def has_https(url):
    return 1 if url.startswith("https") else 0


df["url_length"] = df["url"].apply(url_length)
df["dots"] = df["url"].apply(count_dots)
df["digits"] = df["url"].apply(count_digits)
df["hyphens"] = df["url"].apply(count_hyphens)
df["https"] = df["url"].apply(has_https)

print(df)