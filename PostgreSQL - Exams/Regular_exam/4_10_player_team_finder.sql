CREATE OR REPLACE PROCEDURE sp_players_team_name(IN player_name VARCHAR(50), OUT team_name VARCHAR(45))
AS
$$
BEGIN
	SELECT 
		t.name
	FROM
		players AS p
	LEFT JOIN
		teams AS t
	ON
		p.team_id = t.id
	WHERE
		CONCAT(p.first_name, ' ', p.last_name) = player_name
	INTO team_name;
		
	IF team_name IS NULL THEN
		team_name = 'The player currently has no team';
	END IF;
	RETURN;
END;
$$
LANGUAGE plpgsql;