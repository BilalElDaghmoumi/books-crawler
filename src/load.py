"""Load the clean CSV into a SQLite database."""
import sqlite3

import pandas as pd

df = pd.read_csv("data/clean/books_clean.csv")
with sqlite3.connect("data/books.db") as conn:
    df.to_sql("books", conn, if_exists="replace", index=False)
    count = conn.execute("SELECT COUNT(*) FROM books").fetchone()[0]
print(f"Loaded {count} rows into data/books.db (table: books)")