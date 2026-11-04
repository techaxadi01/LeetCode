-- LeetCode 181: Employees Earning More Than Their Managers
-- Approach: Self JOIN

-- Join Employee table with itself to compare employee salary with manager salary
SELECT e.name AS Employee
FROM Employee e
INNER JOIN Employee m
    ON e.managerId = m.id
WHERE e.salary > m.salary;


/*
Alternative Approach (Implicit JOIN / WHERE Clause):

SELECT e.name AS Employee
FROM Employee e, Employee m
WHERE e.managerId = m.id
  AND e.salary > m.salary;
*/
