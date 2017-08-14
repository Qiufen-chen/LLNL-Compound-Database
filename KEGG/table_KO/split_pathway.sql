DELIMITER $$
DROP PROCEDURE IF EXISTS split_KO_pathway $$
CREATE PROCEDURE split_KO_pathway()
BEGIN
	DECLARE done INT DEFAULT 0;
	DECLARE a VARCHAR(45);
    DECLARE b MEDIUMTEXT;
	DECLARE lstart, lend,max,i INT;
	DECLARE cur CURSOR FOR SELECT Entry,Pathway FROM KEGG.KO;
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
		INSERT INTO KEGG.KO_Pathway(KO_ENTRY,Pathway) VALUES (a,SUBSTRING_INDEX(SUBSTRING_INDEX(b, ';', i), ';', -1));
		SET i=i+1;
			END WHILE;
	END IF;

END LOOP;

CLOSE cur;

END $$



