-- list numbers with the same score and group
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
