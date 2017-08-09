import pymysql.cursors

connection = pymysql.connect(host='clip.llnl.gov',
                             user='dong8',
		             port=5507,
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # create database
        sql = 'CREATE DATABASE SIDER'
        cursor.execute(sql)
        # choose database
        sql = 'USE SIDER'
        cursor.execute(sql)
        # create the table named UMLS_concept_id
        sql = """CREATE TABLE `SIDER`.`UMLS_concept_id` (
                `UMLS_concept_id` VARCHAR(45) NOT NULL,
                PRIMARY KEY (`UMLS_concept_id`));
        """
        cursor.execute(sql)
        # create the table named meddra
        sql = """CREATE TABLE `meddra` (
                  `UMLS_concept_id` varchar(45) NOT NULL,
                  `MedDRA_id` varchar(45) NOT NULL,
                  `kind_of_term` varchar(45) NOT NULL,
                  `name_of_side_effect` varchar(200) NOT NULL,
                  PRIMARY KEY (`kind_of_term`,`UMLS_concept_id`,`MedDRA_id`,`name_of_side_effect`),
                  KEY `fk_meddra_1_idx` (`UMLS_concept_id`),
                  CONSTRAINT `fk_meddra` FOREIGN KEY (`UMLS_concept_id`) REFERENCES `UMLS_concept_id` (`UMLS_concept_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
                ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
        """
        cursor.execute(sql)
        # create the table named all_side_effect
        sql = """CREATE TABLE `all_side_effect` (
                  `STITCH_compound_id_flat` varchar(45) NOT NULL,
                  `STITCH_compound_id_stereo` varchar(45) NOT NULL,
                  `UMLS_concept_id_for_label` varchar(45) NOT NULL,
                  `MedDRA_concept_type` varchar(45) NOT NULL,
                  `UMLS_concept_id_for_MedDRA_term` varchar(45) NOT NULL,
                  `side_effect_name` varchar(100) NOT NULL,
                  PRIMARY KEY (`STITCH_compound_id_flat`,`STITCH_compound_id_stereo`,`UMLS_concept_id_for_label`,`UMLS_concept_id_for_MedDRA_term`,`side_effect_name`,`MedDRA_concept_type`),
                  KEY `fk_all_side_effect_1_idx` (`UMLS_concept_id_for_label`),
                  KEY `fk_all_side_effect_2_idx` (`UMLS_concept_id_for_MedDRA_term`),
                  CONSTRAINT `fk_all_side_effect_1` FOREIGN KEY (`UMLS_concept_id_for_label`) REFERENCES `UMLS_concept_id` (`UMLS_concept_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
                  CONSTRAINT `fk_all_side_effect_2` FOREIGN KEY (`UMLS_concept_id_for_MedDRA_term`) REFERENCES `UMLS_concept_id` (`UMLS_concept_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
                ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
        """
        cursor.execute(sql)
        # create the table named all_label_side_effect
        sql = """CREATE TABLE `all_label_side_effect` (
                  `STITCH_compound_id_flat` varchar(45) NOT NULL,
                  `STITCH_compound_id_stereo` varchar(45) NOT NULL,
                  `UMLS_concept_id_for_label` varchar(45) NOT NULL,
                  `MedDRA_concept_type` varchar(45) NOT NULL,
                  `UMLS_concept_id_for_MedDRA_term` varchar(45) NOT NULL,
                  `side_effect_name` varchar(100) NOT NULL,
                  `source_label` varchar(100) NOT NULL,
                  PRIMARY KEY (`STITCH_compound_id_stereo`,`UMLS_concept_id_for_label`,`MedDRA_concept_type`,`UMLS_concept_id_for_MedDRA_term`,`side_effect_name`,`source_label`,`STITCH_compound_id_flat`),
                  KEY `all_label_side_effect_idx` (`UMLS_concept_id_for_label`),
                  KEY `fk_all_label_side_effect_2_idx` (`UMLS_concept_id_for_MedDRA_term`),
                  CONSTRAINT `fk_all_label_side_effect_1` FOREIGN KEY (`UMLS_concept_id_for_label`) REFERENCES `UMLS_concept_id` (`UMLS_concept_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
                  CONSTRAINT `fk_all_label_side_effect_2` FOREIGN KEY (`UMLS_concept_id_for_MedDRA_term`) REFERENCES `UMLS_concept_id` (`UMLS_concept_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
                ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
        """
        cursor.execute(sql)
        # create the table named all_indications
        sql = """CREATE TABLE `all_indications` (
                  `STITCH_compound_id_flat` varchar(45) NOT NULL,
                  `UMLS_concept_id_for_label` varchar(45) NOT NULL,
                  `method_of_detection` varchar(45) NOT NULL,
                  `concept_name` varchar(45) NOT NULL,
                  `MedDRA_concept_type` varchar(45) NOT NULL,
                  `UMLS_concept_id_for_MedDRA_term` varchar(45) NOT NULL,
                  `MedDRA_concept_name` varchar(100) NOT NULL,
                  PRIMARY KEY (`STITCH_compound_id_flat`,`UMLS_concept_id_for_label`,`method_of_detection`,`concept_name`,`MedDRA_concept_type`,`UMLS_concept_id_for_MedDRA_term`,`MedDRA_concept_name`),
                  KEY `fk_all_indications_1_idx` (`UMLS_concept_id_for_label`),
                  KEY `fk_all_indications_2_idx` (`UMLS_concept_id_for_MedDRA_term`),
                  CONSTRAINT `fk_all_indications_1` FOREIGN KEY (`UMLS_concept_id_for_label`) REFERENCES `UMLS_concept_id` (`UMLS_concept_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
                  CONSTRAINT `fk_all_indications_2` FOREIGN KEY (`UMLS_concept_id_for_MedDRA_term`) REFERENCES `UMLS_concept_id` (`UMLS_concept_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
                ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
        """
        cursor.execute(sql)
        # create the table named all_label_indications
        sql = """CREATE TABLE `all_label_indications` (
                  `STITCH_compound_id_flat` varchar(45) NOT NULL,
                  `STITCH_compound_id_stereo` varchar(45) NOT NULL,
                  `UMLS_concept_id_for_label` varchar(45) NOT NULL,
                  `method_of_detection` varchar(45) NOT NULL,
                  `concept_name` varchar(45) NOT NULL,
                  `MedDRA_concept_type` varchar(45) NOT NULL,
                  `UMLS_concept_id_for_MedDRA_term` varchar(100) NOT NULL,
                  `source_label` varchar(100) NOT NULL,
                  PRIMARY KEY (`STITCH_compound_id_flat`,`STITCH_compound_id_stereo`,`UMLS_concept_id_for_label`,`method_of_detection`,`concept_name`,`MedDRA_concept_type`,`UMLS_concept_id_for_MedDRA_term`,`source_label`),
                  KEY `fk_all_label_indications_1_idx` (`UMLS_concept_id_for_label`),
                  KEY `fk_all_label_indications_2_idx` (`UMLS_concept_id_for_MedDRA_term`),
                  CONSTRAINT `fk_all_label_indications_1` FOREIGN KEY (`UMLS_concept_id_for_label`) REFERENCES `UMLS_concept_id` (`UMLS_concept_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
                  CONSTRAINT `fk_all_label_indications_2` FOREIGN KEY (`UMLS_concept_id_for_MedDRA_term`) REFERENCES `UMLS_concept_id` (`UMLS_concept_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
                ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
        """
        cursor.execute(sql)
        # create the table named freq
        sql = """CREATE TABLE `freq` (
                  `STITCH_compound_id_flat` varchar(45) NOT NULL,
                  `STITCH_compound_id_stereo` varchar(45) NOT NULL,
                  `UMLS_concept_id_for_label` varchar(45) NOT NULL,
                  `placebo` varchar(45) NOT NULL,
                  `frequency_description` varchar(200) NOT NULL,
                  `frequency_low_bound` varchar(45) NOT NULL,
                  `frequency_high_bound` varchar(45) NOT NULL,
                  `MedDRA_concept_type` varchar(45) NOT NULL,
                  `UMLS_concept_id_for_MedDRA_term` varchar(45) NOT NULL,
                  `side_effect_name` varchar(100) NOT NULL,
                  PRIMARY KEY (`STITCH_compound_id_flat`,`STITCH_compound_id_stereo`,`UMLS_concept_id_for_label`,`UMLS_concept_id_for_MedDRA_term`,`side_effect_name`,`MedDRA_concept_type`,`placebo`,`frequency_low_bound`,`frequency_high_bound`,`frequency_description`),
                  KEY `fk_freq_1_idx` (`UMLS_concept_id_for_label`),
                  KEY `fk_freq_2_idx` (`UMLS_concept_id_for_MedDRA_term`),
                  CONSTRAINT `fk_freq_1` FOREIGN KEY (`UMLS_concept_id_for_label`) REFERENCES `UMLS_concept_id` (`UMLS_concept_id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
                  CONSTRAINT `fk_freq_2` FOREIGN KEY (`UMLS_concept_id_for_MedDRA_term`) REFERENCES `UMLS_concept_id` (`UMLS_concept_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
                ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
        """
        cursor.execute(sql)
        # create the table name ATC_Code_for_side_effect
        sql = """CREATE TABLE `SIDER`.`ATC_Code_for_side_effect` (
                `UMLS_concept_id_for_label` VARCHAR(45) NOT NULL,
                `ATC_Code` VARCHAR(45) NOT NULL,
                PRIMARY KEY (`UMLS_concept_id_for_label`, `ATC_Code`))
                CONSTRAINT `UMLS_concept_id_for_label6` FOREIGN KEY (`UMLS_concept_id_for_label`) REFERENCES `UMLS_concept_id` (`UMLS_concept_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
;
        """
        cursor.execute(sql)
        # create the table name ATC_Code_for_indications
        sql = """CREATE TABLE `ATC_Code_for_indications` (
                `UMLS_concept_id_for_label` varchar(45) NOT NULL,
                `ATC_Code` varchar(45) NOT NULL,
                PRIMARY KEY (`UMLS_concept_id_for_label`,`ATC_Code`)
                CONSTRAINT `UMLS_concept_id_for_label7` FOREIGN KEY (`UMLS_concept_id_for_label`) REFERENCES `UMLS_concept_id` (`UMLS_concept_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
                ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
        """
        cursor.execute(sql)
        ##########################################################################################################
        # create temporary table drug_with_side_effect(need to be dropped after all the data loaded)
        sql = """CREATE TABLE drug_with_side_effect (
                                             UMLS_concept_id_for_label varchar(45) NOT NULL,
                                             ATC_Code mediumtext,
                                             PRIMARY KEY (UMLS_concept_id_for_label)
                                             ) 
        """
        cursor.execute(sql)
        # create temporary table drug_with_indications(need to be dropped after all the data loaded)
        sql = """CREATE TABLE drug_with_indications (
                                     UMLS_concept_id_for_label varchar(45) NOT NULL,
                                     ATC_Code mediumtext,
                                     PRIMARY KEY (UMLS_concept_id_for_label)
                                     ) 
                            """
        cursor.execute(sql)
        connection.commit()

finally:
    connection.close()


