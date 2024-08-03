CREATE OR REPLACE FUNCTION 
	fn_courses_by_client(phone_num VARCHAR(20))
RETURNS INT
AS
$$
DECLARE courses_count INT;
BEGIN
	SELECT INTO courses_count
		COUNT(id)
	FROM
		courses
	WHERE
		courses.client_id = (
			SELECT
				id
			FROM
				clients
			WHERE
				clients.phone_number = phone_num
		);
	RETURN courses_count;	
END;
$$
LANGUAGE plpgsql;