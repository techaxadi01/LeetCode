-- LeetCode 185: Department Top Three Salaries
-- Approach: Correlated Subquery

-- Select employees who have fewer than 3 distinct salaries higher than theirs in the same department
SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d
    ON e.departmentId = d.id
WHERE 3 > (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = e.departmentId
      AND e2.salary > e.salary
);
