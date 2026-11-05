-- LeetCode 626: Exchange Seats
-- Approach: Window Functions (LEAD / LAG)

-- Swap consecutive students using LEAD for odd seats and LAG for even seats
SELECT
    id,
    CASE
        WHEN id % 2 = 1 THEN LEAD(student, 1, student) OVER (ORDER BY id)
        WHEN id % 2 = 0 THEN LAG(student) OVER (ORDER BY id)
    END AS student
FROM Seat;


/*
Alternative Approach (CASE Statement on ID):

SELECT
    CASE
        WHEN id % 2 = 1 AND id < (SELECT MAX(id) FROM Seat) THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id;
*/
