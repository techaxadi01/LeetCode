-- LeetCode 176: Second Highest Salary
-- Approach: Subquery with LIMIT / OFFSET

-- Outer SELECT returns NULL if the subquery produces no rows
SELECT (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1 -- OR just LIMIT 1,1
) AS SecondHighestSalary;


/*
Alternative Approach (Using MAX):

SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (
    SELECT MAX(salary)
    FROM Employee
);
*/
