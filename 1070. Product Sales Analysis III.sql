-- LeetCode 1070: Product Sales Analysis III
-- Approach: Tuple IN Subquery with GROUP BY

-- Select sales details for each product in its earliest recorded year
SELECT
    product_id,
    year AS first_year,
    quantity,
    price
FROM Sales
WHERE (product_id, year) IN (
    SELECT
        product_id,
        MIN(year)
    FROM Sales
    GROUP BY product_id
);
