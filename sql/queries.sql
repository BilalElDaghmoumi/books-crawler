-- 1. How many books are in each category?
SELECT category, COUNT(*) AS books
FROM books
GROUP BY category
ORDER BY books DESC;

-- 2. Average, cheapest and most expensive price by category
SELECT category,
       ROUND(AVG(price_gbp), 2) AS avg_price,
       MIN(price_gbp) AS min_price,
       MAX(price_gbp) AS max_price
FROM books
GROUP BY category
ORDER BY avg_price DESC;

-- 3. Five-star books under £20
SELECT title, category, price_gbp
FROM books
WHERE rating = 5 AND price_gbp < 20
ORDER BY price_gbp;

-- 4. How are ratings distributed?
SELECT rating, COUNT(*) AS books,
       ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM books), 1) AS pct
FROM books
GROUP BY rating
ORDER BY rating;

-- 5. Categories with the best average rating (at least 10 books)
SELECT category, ROUND(AVG(rating), 2) AS avg_rating, COUNT(*) AS books
FROM books
GROUP BY category
HAVING COUNT(*) >= 10
ORDER BY avg_rating DESC;

-- 6. Which categories have the most books out of stock?
SELECT category,
       SUM(1 - in_stock) AS out_of_stock,
       ROUND(100.0 * SUM(1 - in_stock) / COUNT(*), 1) AS pct_out
FROM books
GROUP BY category
ORDER BY pct_out DESC;

-- 7. Data quality check: any books with missing or odd values?
SELECT COUNT(*) AS problem_rows
FROM books
WHERE price_gbp IS NULL OR rating NOT BETWEEN 1 AND 5 OR title IS NULL;