#!/bin/bash
labsToGrade=("lab05" "lab06" "lab07" "lab08")
sections=("AYI" "AYJ")
ta="yournetid"

for s in ${sections[@]}; 
do
	for l in ${labsToGrade[@]};
	do
		./get_grades.sh $s $l $ta
		python3 combine_grades.py $s $l > "${s}_${l}.out"
		rm "${s}_${l}_dev1.out" "${s}_${l}_dev2.out" "${s}_${l}_dev3.out" "${s}_${l}_ews.out"
	done
done

python3 add_to_csv.py


