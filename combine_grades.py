def combine_grades(section, lab):
	grades = {}
	file_names = [
		section + "_" + lab + "_ews.out" ,
		section + "_" + lab + "_dev1.out" ,
		section + "_" + lab + "_dev2.out" ,
		section + "_" + lab + "_dev3.out" ,
	]

	for file in file_names:
		with open(file, "r") as f:
			for line in f.readlines():
				splits = line.split('\t')
				if len(splits) != 2:
					continue
				else:
					netid = splits[0]
					grade = float(splits[1])
					if netid in grades:
						grades[netid] = max(grades[netid], grade)
					else:
						grades[netid] = grade

	for k in sorted(grades.keys()):
		print(k,"\t", grades[k])


if __name__ == "__main__":
	import sys
	section = sys.argv[1]
	lab = sys.argv[2]
	combine_grades(section, lab)