# books-crawler# Books Pipeline: a small end-to-end data project

Generates a realistic, messy book catalogue (1,025 raw rows, the same shape as
scraped web data), cleans and validates it with pandas, loads it into SQLite
and answers business questions with SQL.

## Why synthetic data?
The generator produces data that looks like what a web crawler would collect:
prices as text ("£20.98"), ratings as words ("Three"), messy whitespace and
duplicate rows. A fixed random seed means anyone who clones the repository gets
identical data and identical results.

## Pipeline
1. `src/generate_data.py`: creates the raw CSV, with deliberate quality issues
2. `src/clean.py`: converts text to typed columns, removes duplicates, runs data quality checks
3. `src/load.py`: loads the clean data into `data/books.db` (rerunnable, replaces the table)
4. `sql/queries.sql`: seven analysis and quality queries
5. `src/run_queries.py`: runs every query and prints the results

## How to run
```
pip install -r requirements.txt
python src/generate_data.py
python src/clean.py
python src/load.py
python src/run_queries.py
```

## Data quality checks
The cleaning script stops with an error if any check fails:
- 25 duplicate rows detected and removed by URL, leaving 1,000 books
- No missing or negative prices
- All ratings between 1 and 5
- A final SQL check confirms 0 problem rows in the database

## Key findings
- **Most expensive category on average:** Religion (£37.80)
- **Largest category:** Science Fiction (62 books)
- **Five-star books:** 20.2% of the catalogue; 40 of them cost under £20
- **Highest out-of-stock rate:** Sports (19.6% of its books)
- **Note:** ratings are almost evenly spread (about 20% each), as expected from
  uniformly random synthetic data. Real catalogue data would usually be skewed.

## Tools
Python, pandas, SQLite, SQL, Git, GitHub Codespaces