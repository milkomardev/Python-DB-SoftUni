CREATE OR REPLACE FUNCTION fn_get_volunteers_count_from_department(searched_volunteers_department VARCHAR(30))
RETURNS INT
AS
$$
DECLARE volunteers_count INT;
BEGIN
	SELECT
		COUNT(*) INTO volunteers_count
	FROM
		volunteers_departments AS vd
	JOIN
		volunteers AS v
	ON
		vd.id = v.department_id
	WHERE
		vd.department_name = searched_volunteers_department;
	RETURN volunteers_count;
END;
$$
LANGUAGE plpgsql;