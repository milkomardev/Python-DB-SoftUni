CREATE TABLE search_results (
    id SERIAL PRIMARY KEY,
    address_name VARCHAR(50),
    full_name VARCHAR(100),
    level_of_bill VARCHAR(20),
    make VARCHAR(30),
    condition CHAR(1),
    category_name VARCHAR(50)
);


CREATE OR REPLACE PROCEDURE sp_courses_by_address(IN address_name VARCHAR(100))
AS
$$
	BEGIN
		TRUNCATE search_results;
		
		INSERT INTO search_results(
			address_name, 
			full_name, 
			level_of_bill, 
			make, 
			condition, 
			category_name
		)
		SELECT
			a.name,
			cl.full_name,
			CASE
				WHEN cou.bill <= 20 THEN 'Low'
				WHEN cou.bill <= 30 THEN 'Medium'
				ELSE 'High'
			END AS level_of_bill,
			ca.make,
			ca.condition,
			cat.name
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
			cars AS ca
		ON
			cou.car_id = ca.id
		JOIN
			categories AS cat
		ON
			ca.category_id = cat.id
		WHERE
			a.name = address_name
		ORDER BY
			ca.make,
			cl.full_name;
	END;
$$
LANGUAGE plpgsql;