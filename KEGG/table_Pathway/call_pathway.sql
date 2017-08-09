set sql_safe_updates = 0;
call split_Pathway_compound();
select * from KEGG.Pathway_Compound;

call split_Pathway_module();
select * from KEGG.Pathway_Module;

call split_Pathway_disease();
select * from KEGG.Pathway_Disease;

call split_Pathway_drug();
select * from KEGG.Pathway_Drug;

call split_Pathway_enzyme();
select * from KEGG.Pathway_Enzyme;

call split_Pathway_gene();
select * from KEGG.Pathway_Gene;

call split_Pathway_orthology();
select * from KEGG.Pathway_Orthology;

call split_Pathway_reaction();
select * from KEGG.Pathway_Reaction;



