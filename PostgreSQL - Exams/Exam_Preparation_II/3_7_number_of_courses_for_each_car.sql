SELECT
	cars.id AS car_id,
	cars.make,
	cars.mileage,
	COUNT(co.id) AS count_of_courses,
	ROUND(AVG(co.bill), 2) AS average_bill
FROM
	cars
LEFT JOIN
	courses AS co
ON
	cars.id = co.car_id
GROUP BY
	cars.id
HAVING
	COUNT(co.id) <> 2
ORDER BY
	count_of_courses DESC,
	car_id
;
	
