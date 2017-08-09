set sql_safe_updates = 0;
select * from  KEGG.Module where Entry = 'aace_M00616';
-- where Entry =  'aaa_M00176';

call split_Module_brite();
select * from  KEGG.Module_Brite;

call split_Module_compound();
select * from  KEGG.Module_Compound;

call split_Module_gene();
select * from  KEGG.Module_Gene;

call split_Module_orthology();
select * from   KEGG.Module_Orthology;

call split_Module_pathway();
select * from  KEGG.Module_Pathway;

call split_Module_reaction();
select * from  KEGG.Module_Reaction;

call split_Module_refmodule();
select * from  KEGG.Module_Ref_Module;

call split_Module_rmodule();
select * from  KEGG.Module_Rmodule;

UPDATE `KEGG`.`Module` SET `Orthology`='K00860;K00955;K00957;K00392;K00958;K13811;K00390;K02045;K02047;K02046;K02048;K00380;K00381;K00956' WHERE (substring(Entry,-6,6) = 'M00616');


