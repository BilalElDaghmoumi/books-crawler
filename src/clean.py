"""Turn raw scraped text into typed columns and run data quality checks."""
from pathlib import Path

import pandas as pd

RAW = Path("data/raw/books_raw.csv")
OUT = Path("data/clean/books_clean.csv")
RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

df = pd.read_csv(RAW)

# 1. Convert text to proper types
df["price_gbp"] = df["price_raw"].str.replace(r"[^0-9.]", "", regex=True).astype(float)
df["rating"] = df["rating_raw"].map(RATINGS)
df["in_stock"] = df["availability_raw"].str.contains("In stock")
df["title"] = df["title"].str.strip()

# 2. Remove duplicates (the URL identifies each book)
before = len(df)
df = df.drop_duplicates(subset="url")

# 3. Data quality checks: stop with a clear message if anything is wrong
checks = {
    "duplicates removed": before - len(df),
    "rows": len(df),
    "missing prices": int(df["price_gbp"].isna().sum()),
    "ratings outside 1-5": int((~df["rating"].between(1, 5)).sum()),
    "negative prices": int((df["price_gbp"] < 0).sum()),
}
print(checks)
assert checks["missing prices"] == 0, "Some prices could not be parsed"
assert checks["ratings outside 1-5"] == 0, "Unexpected rating values"
assert checks["negative prices"] == 0, "Negative prices found"
if checks["rows"] != 1000:
    print("Warning: expected 1,000 books - check the data source")

# 4. Save only the clean columns
OUT.parent.mkdir(parents=True, exist_ok=True)
df[["title", "category", "price_gbp", "rating", "in_stock", "url"]].to_csv(OUT, index=False)
print(f"Saved {len(df)} clean rows to {OUT}")