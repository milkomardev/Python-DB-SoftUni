UPDATE 
	coaches
SET
	salary = coach_level * salary
WHERE
	(SELECT 
		COUNT(pc.player_id)
	FROM 
		players_coaches AS pc
	JOIN
		coaches AS c
	ON 
		c.id = pc.coach_id
	WHERE
		c.first_name LIKE('C%')
	GROUP BY
		coach_id) > 0