"""Generate a fake, slightly messy book catalogue that looks like scraped data."""
import random
from pathlib import Path

import pandas as pd

OUT = Path("data/raw/books_raw.csv")
N_BOOKS = 1000
N_DUPLICATES = 25

CATEGORIES = [
    "Mystery", "Romance", "Fantasy", "Science Fiction", "History",
    "Travel", "Poetry", "Business", "Biography", "Horror",
    "Cookbooks", "Self Help", "Childrens", "Philosophy", "Art",
    "Sports", "Music", "Health", "Politics", "Religion",
]
ADJECTIVES = ["Silent", "Hidden", "Lost", "Golden", "Broken", "Last", "Wild",
              "Secret", "Burning", "Quiet", "Endless", "Forgotten"]
NOUNS = ["River", "Garden", "City", "Kingdom", "Letter", "Journey", "Shadow",
         "Island", "Promise", "Winter", "Machine", "Mountain"]
RATINGS = ["One", "Two", "Three", "Four", "Five"]

random.seed(42)  # same "random" data every run


def make_book(i):
    title = f"The {random.choice(ADJECTIVES)} {random.choice(NOUNS)}"
    if random.random() < 0.05:
        title = f"  {title}  "  # messy whitespace, like real scraped text
    slug = title.strip().lower().replace(" ", "-")
    if random.random() < 0.9:
        availability = f"In stock ({random.randint(1, 25)} available)"
    else:
        availability = "Out of stock"
    return {
        "title": title,
        "category": random.choice(CATEGORIES),
        "price_raw": f"£{random.uniform(10, 60):.2f}",
        "rating_raw": random.choice(RATINGS),
        "availability_raw": availability,
        "url": f"https://books.example.com/catalogue/{slug}_{i}/index.html",
    }


rows = [make_book(i) for i in range(1, N_BOOKS + 1)]
rows += random.sample(rows, N_DUPLICATES)  # duplicates, like a crawler revisiting pages
random.shuffle(rows)

OUT.parent.mkdir(parents=True, exist_ok=True)
pd.DataFrame(rows).to_csv(OUT, index=False)
print(f"Saved {len(rows)} rows ({N_DUPLICATES} duplicates) to {OUT}")