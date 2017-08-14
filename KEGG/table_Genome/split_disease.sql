DELIMITER $$
DROP PROCEDURE IF EXISTS split_Genome_disease $$
CREATE PROCEDURE split_Genome_disease()
BEGIN
	DECLARE done INT DEFAULT 0;
	DECLARE a VARCHAR(45);
    DECLARE b MEDIUMTEXT;
	DECLARE lstart, lend,max,i INT;
	DECLARE cur CURSOR FOR SELECT Entry,Disease FROM KEGG.Genome;
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
		INSERT INTO KEGG.Genome_Disease(Entry,Disease) VALUES (a,SUBSTRING_INDEX(SUBSTRING_INDEX(b, ';', i), ';', -1));
		SET i=i+1;
			END WHILE;
	END IF;

END LOOP;

CLOSE cur;

END $$



