DELIMITER $$
DROP PROCEDURE IF EXISTS split_Compound_drug_group $$
CREATE PROCEDURE split_Compound_drug_group()
BEGIN
	DECLARE done INT DEFAULT 0;
	DECLARE a VARCHAR(45);
	DECLARE lstart, lend INT;
	DECLARE b MEDIUMTEXT;
	DECLARE cur CURSOR FOR SELECT Entry,Drug_Group FROM KEGG.Compound;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

	OPEN cur;
	read_loop: LOOP

		FETCH cur INTO a, b;
		IF done THEN
			LEAVE read_loop;
		END IF;
		-- Keep all using the same format
		SET b = REPLACE(b, ",", ";");
		SET b = REPLACE(b, "+", ";");
		SET lstart = 1;
		SET lend = LOCATE(";", b, lstart);
		WHILE lend > 0 DO
			INSERT INTO KEGG.Compound_Drug_Group(Entry,Drug_Group) VALUES (a,SUBSTRING(b, lstart, lend-lstart));
			SET lstart = lend+1;
			SET lend = LOCATE(";", b, lstart);
		END WHILE;
		IF b <> "" THEN
			INSERT INTO KEGG.Compound_Drug_Group(Entry,Drug_Group) VALUES (a, SUBSTRING(b, lstart));
		END IF;
		
	END LOOP;
	CLOSE cur;
END;


