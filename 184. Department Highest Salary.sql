-- LeetCode 184: Department Highest Salary
-- Approach: Correlated Subquery with JOIN

-- Find employees whose salary equals the maximum salary of their department
SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Department d
JOIN Employee e
    ON e.departmentId = d.id
WHERE e.salary = (
    SELECT MAX(e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = e.departmentId
);
