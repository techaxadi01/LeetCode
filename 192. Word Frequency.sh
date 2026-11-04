# LeetCode 192: Word Frequency
# Approach: Unix Pipeline (tr + sort + uniq + awk)

# Split words into individual lines, count occurrences, and sort descending
tr -s '[:space:]' '\n' < words.txt | \
    grep -v '^$' | \
    sort | \
    uniq -c | \
    sort -rn | \
    awk '{print $2, $1}'
