-- LeetCode 602: Friend Requests II: Who Has the Most Friends
-- Approach: UNION ALL with GROUP BY and LIMIT

-- Combine requesters and accepters to count total friendship connections per person
SELECT
    id,
    COUNT(*) AS num
FROM (
    SELECT requester_id AS id FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id FROM RequestAccepted
) all_friends
GROUP BY id
ORDER BY num DESC
LIMIT 1;
