import pymysql.cursors

connection = pymysql.connect(host='clip.llnl.gov',
                             user='dong8',
                             port=5507,
                             cursorclass=pymysql.cursors.DictCursor)

with open("meddra.tsv") as fh1:
    a = 0
    for line in fh1:
        col1 = line.split('\t')[0]
        col2 = line.split('\t')[1]
        col3 = line.split('\t')[2]
        col4 = line.split('\t')[3]
        a += 1
        with connection.cursor() as cursor:
            sql = "SET sql_safe_updates = 0"
            cursor.execute(sql)
            sql = 'use SIDER'
            cursor.execute(sql)
            sql = '''insert into meddra(UMLS_concept_id,
                                        MedDRA_id,
                                        kind_of_term,
                                        name_of_side_effect
                                                 )
                     values (%s,%s,%s,%s)'''
            cursor.execute(sql, (col1, col2, col3, col4))
            connection.commit()
            print a,"meddra loaded"

with open("meddra_all_se.tsv") as fh2:
    b = 0
    for line in fh2:
        col1 = line.split('\t')[0]
        col2 = line.split('\t')[1]
        col3 = line.split('\t')[2]
        col4 = line.split('\t')[3]
        col5 = line.split('\t')[4]
        col6 = line.split('\t')[5]
        b += 1
        with connection.cursor() as cursor:
            sql = "SET sql_safe_updates = 0"
            cursor.execute(sql)
            sql = 'use SIDER'
            cursor.execute(sql)
            sql = '''insert into all_side_effect(STITCH_compound_id_flat,
                                       STITCH_compound_id_stereo,
                                       UMLS_concept_id_for_label,
                                       MedDRA_concept_type,
                                       UMLS_concept_id_for_MedDRA_term,
                                       side_effect_name)
                    values (%s,%s,%s,%s,%s,%s)'''
            cursor.execute(sql, (col1, col2, col3, col4, col5, col6))
            connection.commit()
            print b,"all_se loaded"

with open("meddra_all_label_se.tsv") as fh3:
    c = 0
    for line in fh3:
        col1 = line.split('\t')[1]
        col2 = line.split('\t')[2]
        col3 = line.split('\t')[3]
        col4 = line.split('\t')[4]
        col5 = line.split('\t')[5]
        col6 = line.split('\t')[6]
        col7 = line.split('\t')[0]
        c += 1
        with connection.cursor() as cursor:
            sql = "SET sql_safe_updates = 0"
            cursor.execute(sql)
            sql = 'use SIDER'
            cursor.execute(sql)
            sql = '''insert into all_label_side_effect(STITCH_compound_id_flat,
                                        STITCH_compound_id_stereo,
                                        UMLS_concept_id_for_label,
                                        MedDRA_concept_type,
                                        UMLS_concept_id_for_MedDRA_term,
                                        side_effect_name,
                                        source_label)
                     values (%s,%s,%s,%s,%s,%s,%s)'''
            cursor.execute(sql, (col1, col2, col3, col4, col5, col6, col7))
            connection.commit()
            print c,"all_label_se loaded"

with open("meddra_all_indications.tsv") as fh4:
    d = 0
    for line in fh4:
        col1 = line.split('\t')[0]
        col2 = line.split('\t')[1]
        col3 = line.split('\t')[2]
        col4 = line.split('\t')[3]
        col5 = line.split('\t')[4]
        col6 = line.split('\t')[5]
        col7 = line.split('\t')[6]
        d += 1
        with connection.cursor() as cursor:
            sql = "SET sql_safe_updates = 0"
            cursor.execute(sql)
            sql = 'use SIDER'
            cursor.execute(sql)
            sql = '''insert into all_indications(STITCH_compound_id_flat,
                                                 UMLS_concept_id_for_label,
                                                 method_of_detection,
                                                 concept_name,
                                                 MedDRA_concept_type,
                                                 UMLS_concept_id_for_MedDRA_term,
                                                 MedDRA_concept_name)
                     values (%s,%s,%s,%s,%s,%s,%s)'''
            cursor.execute(sql, (col1, col2, col3, col4, col5, col6, col7))
            connection.commit()
            print d,"all_indications loaded"

with open("meddra_all_label_indications.tsv") as fh5:
    e = 0
    for line in fh5:
        col1 = line.split('\t')[1]
        col2 = line.split('\t')[2]
        col3 = line.split('\t')[3]
        col4 = line.split('\t')[4]
        col5 = line.split('\t')[5]
        col6 = line.split('\t')[6]
        col7 = line.split('\t')[7]
        col8 = line.split('\t')[0]
        e += 1
        with connection.cursor() as cursor:
            sql = "SET sql_safe_updates = 0"
            cursor.execute(sql)
            sql = 'use SIDER'
            cursor.execute(sql)
            sql = '''insert into all_label_indications(STITCH_compound_id_flat,
                                                 STITCH_compound_id_stereo,
                                                 UMLS_concept_id_for_label,
                                                 method_of_detection,
                                                 concept_name,
                                                 MedDRA_concept_type,
                                                 UMLS_concept_id_for_MedDRA_term,
                                                 source_label)
                     values (%s,%s,%s,%s,%s,%s,%s,%s)'''
            cursor.execute(sql, (col1, col2, col3, col4, col5, col6, col7, col8))
            connection.commit()
            print e,"all_label_indications loaded"

with open("meddra_freq.tsv") as fh6:
    f = 0
    for line in fh6:
        col1 = line.split('\t')[0]
        col2 = line.split('\t')[1]
        col3 = line.split('\t')[2]
        col4 = line.split('\t')[3]
        col5 = line.split('\t')[4]
        col6 = line.split('\t')[5]
        col7 = line.split('\t')[6]
        col8 = line.split('\t')[7]
        col9 = line.split('\t')[8]
        col10 = line.split('\t')[9]
        f += 1
        with connection.cursor() as cursor:
            sql = "SET sql_safe_updates = 0"
            cursor.execute(sql)
            sql = 'use SIDER'
            cursor.execute(sql)
            sql = '''insert into freq(STITCH_compound_id_flat,
                                        STITCH_compound_id_stereo,
                                        UMLS_concept_id_for_label,
                                        placebo,
                                        frequency_description,
                                        frequency_low_bound,
                                        frequency_high_bound,
                                        MedDRA_concept_type,
                                        UMLS_concept_id_for_MedDRA_term,
                                        side_effect_name)
                     values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            cursor.execute(sql, (col1, col2, col3, col4, col5, col6, col7, col8, col9, col10))
            connection.commit()
            print f,"freq load"
connection.close()



