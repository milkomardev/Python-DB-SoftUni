SELECT
	o.name AS owner, 
	count(a.animal_type_id) AS count_of_animals
FROM
	owners AS o
JOIN
	animals AS a
ON
	a.owner_id = o.id
GROUP BY
	o.name
ORDER BY
	count_of_animals DESC,
	o.name
LIMIT
	5
;