-- LeetCode 627: Swap Sex of Employees
-- Approach: CASE Statement

-- Swap 'm' with 'f' and vice versa in a single UPDATE statement
UPDATE Salary
SET sex = CASE
    WHEN sex = 'm' THEN 'f'
    WHEN sex = 'f' THEN 'm'
END;


/*
Alternative Approach (MySQL IF function):

UPDATE Salary
SET sex = IF(sex = 'm', 'f', 'm');
*/
