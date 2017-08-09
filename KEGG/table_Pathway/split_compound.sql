DELIMITER $$
DROP PROCEDURE IF EXISTS split_Pathway_compound $$
CREATE PROCEDURE split_Pathway_compound()
BEGIN
	DECLARE done INT DEFAULT 0;
	DECLARE a VARCHAR(45);
    DECLARE b MEDIUMTEXT;
	DECLARE lstart, lend,max,i INT;
	DECLARE cur CURSOR FOR SELECT Entry,Compound FROM KEGG.Pathway;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1;

	OPEN cur;
    read_loop: LOOP
    FETCH cur INTO a, b;
    
    SET i = 1;
    SET max = 1+ length(b)-length(replace(b,';',''));
    
    IF done=1 THEN
		LEAVE read_loop;
		END IF;	
	
    IF max > 0 THEN
		WHILE i <= max DO
		INSERT INTO KEGG.Pathway_Compound(Entry,Compound) VALUES (a,SUBSTRING_INDEX(SUBSTRING_INDEX(b, ';', i), ';', -1));
		SET i=i+1;
			END WHILE;
	END IF;

END LOOP;

CLOSE cur;

END $$