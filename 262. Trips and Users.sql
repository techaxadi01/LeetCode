-- LeetCode 262: Trips and Users
-- Approach: JOIN with Filter and AVG Cancellation

-- Calculate daily cancellation rate for unbanned users between Oct 1 and Oct 3, 2013
SELECT
    t.request_at AS Day,
    ROUND(AVG(t.status != 'completed'), 2) AS `Cancellation Rate`
FROM Trips t
JOIN Users c
    ON t.client_id = c.users_id
JOIN Users d
    ON t.driver_id = d.users_id
WHERE c.banned = 'No'
  AND d.banned = 'No'
  AND t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY t.request_at;
