-- LeetCode 620: Not Boring Movies
-- Approach: WHERE Filtering with Modulo and ORDER BY

-- Filter movies with an odd-numbered ID and non-boring description
SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description != 'boring'
ORDER BY rating DESC;
