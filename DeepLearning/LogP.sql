-- select LogP

select * from chembl_23.activities where standard_type = 'LogP' and standard_units is null;

select c.chembl_id 
		  ,a.standard_value
          ,b.canonical_smiles
from chembl_23.activities a 
join chembl_23.compound_structures b
		  on a.molregno = b.molregno
join  chembl_23.molecule_dictionary c
		  on b.molregno = c.molregno
join chembl_23.chembl_id_lookup d
		  on c.chembl_id = d.chembl_id
join chembl_23.compound_properties e
		  on c.molregno = e.molregno
where a.standard_type = 'LogP' and a.standard_units is null and e.hba <= 10 and e.hbd <= 5 and  e.mw_freebase  between 180 and 500
and  c.chembl_id is not null
and a.standard_value is not null
and b.canonical_smiles is not null
into outfile '/tmp/LogP_null.csv'
fields terminated by ','
optionally enclosed by '"'
lines terminated by '\n';