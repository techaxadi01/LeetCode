-- LeetCode 197: Rising Temperature
-- Approach: Self JOIN with DATEDIFF

-- Find all dates with higher temperatures compared to their previous day
SELECT w1.id
FROM Weather w1
JOIN Weather w2
    ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
