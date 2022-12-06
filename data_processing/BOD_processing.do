clear

use "/Users/eloiseburtis/Desktop/Econometrics Demo/Prowess Raw Files/full_BOD.dta"

//drop observations where committee is not the board of directors (this cuts data size down by approx 2/3 from 2.87 mil observations to 1.02 mil observations)
drop if committee_name != "Board of directors"

//reshape data frame so that there is only one row per company per year

reshape wide 

//create promotor dummy variable (treat N/A as non-promoter)
gen promoter = (prom_non_prom_category == "Promoter")

//create ceo_duality dummy variable
gen ceo_duality = (designation_full_name == "Chairperson, Managing Director & Chief Executive Officer" || designation_full_name == "Chairperson & Chief Executive Officer")

//drop unneccessary variables
drop committee_name corpdiro_din designation_full_name category board_meetings_attended salary sitting_fees contrib_to_pf bonus_commission perquisites retirement_benefits tot_remuneration exec_non_exec_category prom_non_prom_category no_of_oth_cos_chairperson has_resigned no_of_committee_pos_held has_retired last_agm_attended appointment_date resignation_date no_of_oth_cos_director corpdiro_desig_seqno indep_non_indep_category


//this should work to reshape the data --> not sure why I am having issues with missing values
reshape wide promoter ceo_duality, i(co_code company_name corpdiro_date) j(directors_name) string
