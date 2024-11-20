/* this statement selects all player IDs that have a total goal number greater than the average of all goals */
SELECT player_id, SUM(goals) AS total_goals
FROM Match_Stats 
GROUP BY player_id
HAVING SUM(goals) > (
	SELECT AVG(SUM(goals))
	FROM Match_Stats
	GROUP BY player_id
);

/* selects all player IDs that have played in more than one match */
SELECT player_id, COUNT(match_id) AS total_games
FROM Match_Stats
GROUP BY player_id
HAVING COUNT(match_id) > 1;

/* selects the first name and last name of all users who are either players or referees and combines the results of both queries */
SELECT 
    (SELECT u.first_name FROM users u WHERE u.user_id = p.player_id) AS first_name,
    (SELECT u.last_name FROM users u WHERE u.user_id = p.player_id) AS last_name
FROM players p
UNION
SELECT 
    (SELECT u.first_name FROM users u WHERE u.user_id = r.referee_id) AS first_name,
    (SELECT u.last_name FROM users u WHERE u.user_id = r.referee_id) AS last_name
FROM referees r;

/* selects the player ID, first name, and last name of all players who have scored at least one goal */
SELECT 
    p.player_id,
    (SELECT u.first_name FROM users u WHERE u.user_id = p.player_id) AS first_name,
    (SELECT u.last_name FROM users u WHERE u.user_id = p.player_id) AS last_name
FROM players p
WHERE EXISTS (
    SELECT 1
    FROM match_stats ms
    WHERE ms.player_id = p.player_id
    AND ms.goals > 0
);

/* selects the player ID of all players who do not have any match_stats records */
SELECT player_id FROM Players 
MINUS
SELECT player_id FROM Match_Stats;
