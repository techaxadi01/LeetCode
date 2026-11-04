-- LeetCode 178: Rank Scores
-- Approach: Window Function (DENSE_RANK)

-- DENSE_RANK assigns consecutive ranks without gaps for ties
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank'
FROM Scores
ORDER BY score DESC;


/*
Alternative Approach (Correlated Subquery):

SELECT
    s1.score,
    (
        SELECT COUNT(DISTINCT s2.score)
        FROM Scores s2
        WHERE s2.score >= s1.score
    ) AS 'rank'
FROM Scores s1
ORDER BY s1.score DESC;
*/
