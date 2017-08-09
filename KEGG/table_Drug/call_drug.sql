call split_Drug_drug_group();
select * from KEGG.Drug_Drug_Group;

call split_Drug_compound();
select * from KEGG.Drug_Compound;

call split_Drug_therapeutic_category();
select * from KEGG.Drug_Therapeutic_Category;

call split_Drug_atc_code();
select * from KEGG.Drug_ATC_Code;

call split_Drug_all_map();
select * from KEGG.Drug_All_Map;

