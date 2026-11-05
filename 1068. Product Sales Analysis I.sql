-- LeetCode 1068: Product Sales Analysis I
-- Approach: INNER JOIN

-- Match each sale with its corresponding product name
SELECT
    p.product_name,
    s.year,
    s.price
FROM Sales s
JOIN Product p
    ON s.product_id = p.product_id;

