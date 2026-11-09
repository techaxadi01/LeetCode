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



/*
Alternative Approach (NOT EXISTS / Relational Division):

SELECT DISTINCT c.customer_id
FROM Customer c
WHERE NOT EXISTS (
    SELECT p.product_key
    FROM Product p
    WHERE NOT EXISTS (
        SELECT 1
        FROM Customer c2
        WHERE c2.customer_id = c.customer_id
          AND c2.product_key = p.product_key
    )
);
*/
