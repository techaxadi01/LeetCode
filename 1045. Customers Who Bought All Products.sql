-- LeetCode 1045: Customers Who Bought All Products
-- Approach: GROUP BY with HAVING COUNT(DISTINCT)

-- Select customers who purchased every distinct product available
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(*)
    FROM Product
);
