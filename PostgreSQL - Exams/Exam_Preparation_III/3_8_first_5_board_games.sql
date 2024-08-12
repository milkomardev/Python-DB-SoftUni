SELECT
	bg.name,
	bg.rating,
	c.name AS category_name
FROM
	board_games AS bg
JOIN
	players_ranges AS pr
ON
	bg.players_range_id = pr.id
JOIN
	categories AS c
ON	
	bg.category_id = c.id
WHERE
	(bg.rating > 7.00 
		AND 
	(bg.name LIKE '%A%' OR bg.name LIKE'%a%'))
			OR
	(bg.rating > 7.50
		AND
	(pr.min_players = 2 AND pr.max_players = 5))
ORDER BY
	bg.name,
	bg.rating DESC
LIMIT
	5