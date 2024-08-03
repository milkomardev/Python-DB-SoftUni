SELECT
	a.name AS address,
	CASE
		WHEN EXTRACT(HOUR FROM cou.start) BETWEEN 6 AND 20 THEN 'Day'
		ELSE 'Night'		
	END AS day_time,
	cou.bill,
	cl.full_name,
	cars.make,
	cars.model,
	cat.name AS category_name
FROM
	courses AS cou
JOIN
	addresses AS a
ON 
	a.id = cou.from_address_id
JOIN
	clients AS cl
ON
	cou.client_id = cl.id
JOIN
	cars
ON
	cou.car_id = cars.id
JOIN
	categories AS cat
ON
	cars.category_id = cat.id
ORDER BY
	cou.id
	