-- LeetCode 577: Employee Bonus
-- Approach: LEFT JOIN with IS NULL Check

-- LEFT JOIN ensures employees without a bonus record (NULL) are included
SELECT
    e.name,
    b.bonus
FROM Employee e
LEFT JOIN Bonus b
    ON e.empId = b.empId
WHERE b.bonus < 1000
   OR b.bonus IS NULL;


/*
Alternative Approach (Using IFNULL / COALESCE):

SELECT
    e.name,
    b.bonus
FROM Employee e
LEFT JOIN Bonus b
    ON e.empId = b.empId
WHERE IFNULL(b.bonus, 0) < 1000;
*/
