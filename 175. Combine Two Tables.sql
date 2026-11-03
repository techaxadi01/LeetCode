-- LeetCode 175: Combine Two Tables
-- Approach: LEFT JOIN

-- LEFT JOIN ensures every person is included, even without an address entry
SELECT
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a
    ON p.personId = a.personId;
