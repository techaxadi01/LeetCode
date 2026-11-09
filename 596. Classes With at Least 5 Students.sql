-- LeetCode 596: Classes With at Least 5 Students
-- Approach: GROUP BY with HAVING COUNT

-- Find all classes that have at least 5 students enrolled
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;
