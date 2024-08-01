SELECT
	a.name AS animal,
	EXTRACT('year' FROM a.birthdate) AS birth_year,
	at.animal_type AS animal_type
FROM
	animals AS a
JOIN
	animal_types AS at
ON
	a.animal_type_id = at.id
	
WHERE
	at.animal_type <> 'Birds'
		AND
	a.owner_id IS NULL
		AND
	AGE('01/01/2022', a.birthdate) < '5 years'
ORDER BY
	a.name
;