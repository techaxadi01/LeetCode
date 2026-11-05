-- LeetCode 584: Find Customer Referee
-- Approach: WHERE with IS NULL Check

-- Return customers who are not referred by customer with id = 2 (including NULL)
SELECT name
FROM Customer
WHERE referee_id != 2
   OR referee_id IS NULL;
   