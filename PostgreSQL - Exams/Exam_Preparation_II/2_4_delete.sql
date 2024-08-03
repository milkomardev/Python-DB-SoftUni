DELETE FROM 
	clients
WHERE
	CHAR_LENGTH(full_name) > 3
		AND
	id NOT IN (
				SELECT
					client_id
				FROM
					courses
			)
;