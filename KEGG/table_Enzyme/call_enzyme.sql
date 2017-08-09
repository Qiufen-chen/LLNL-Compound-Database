call split_Enzyme_all_reac();
select * from KEGG.Enzyme_All_Reac;

call split_Enzyme_orthology();
select * from KEGG.Enzyme_Orthology;

call split_Enzyme_pathway();
select * from KEGG.Enzyme_Pathway;

call split_Enzyme_product();
select * from KEGG.Enzyme_Product;

call split_Enzyme_substrate();
select * from KEGG.Enzyme_Substrate;