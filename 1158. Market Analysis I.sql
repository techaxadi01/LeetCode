-- LeetCode 1158: Market Analysis I
-- Approach: LEFT JOIN with COUNT and YEAR()

-- Filter 2019 orders in the ON clause to keep all users (even with 0 orders)
SELECT
    u.user_id AS buyer_id,
    u.join_date,
    COUNT(o.order_id) AS orders_in_2019
FROM Users u
LEFT JOIN Orders o
    ON u.user_id = o.buyer_id
    AND YEAR(o.order_date) = 2019
GROUP BY u.user_id, u.join_date;
