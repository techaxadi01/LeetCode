-- LeetCode 183: Customers Who Never Order
-- Approach: NOT IN Subquery

-- Filter out customers whose IDs exist in the Orders table
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId
    FROM Orders
);


/*
Alternative Approach (LEFT JOIN / IS NULL):

SELECT c.name AS Customers
FROM Customers c
LEFT JOIN Orders o
    ON c.id = o.customerId
WHERE o.customerId IS NULL;
*/
