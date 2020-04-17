import os

def combine_grades(section, lab, ta_id, passwd):
	grades = {}
	file_names = [
		section + "_" + lab + "_ews.out",
		section + "_" + lab + "_dev1.out",
		section + "_" + lab + "_dev2.out",
		section + "_" + lab + "_dev3.out",
	]

	servers = [
		ta_id + "@cs101-dev-01.cs.illinois.edu",
		ta_id + "@cs101-dev-02.cs.illinois.edu",
		ta_id + "@cs101-dev-03.cs.illinois.edu",
		# ta_id + "@linux.ews.illinois.edu",
	]

	missing_grades = set()

	for file in file_names:
		with open(file, "r") as f:
			for line in f.readlines():
				splits = line.split("\t")
				if len(splits) != 2:
					if "No grade found for" in line:
						missing_netid = line.split(" ")[4][:-2]
						# print(missing_netid)
						missing_grades.add(missing_netid)
					continue
				else:
					netid = splits[0]
					grade = float(splits[1])
					if netid in grades:
						grades[netid] = max(grades[netid], grade)
					else:
						grades[netid] = grade

	for k in sorted(grades.keys()):
		print(k, "\t", grades[k])
		missing_grades.remove(k)
	# print(missing_grades)
	print("total graded: ", len(grades), "Missing grades:", len(missing_grades))

	# For all the missing grades, check whether they submitted
	def check_submission(netid, lab, server, passwd):
		cmd = (
			"ssh "
			+ server
			+ ' "echo '
			+ passwd
			+ " | sudo -S ls /class/cs101/tmp/exchange/cs101/inbound | grep "
			+ netid
			+ "+"
			+ lab
			+ "\""
		)
		print(cmd)
		stream = os.popen(cmd)
		output = stream.read()
		if netid in output and lab in output:
			return True
		return False
		# return cmd

	submitted_but_not_graded = set()
	# print(check_submission("jlondon3", "lab08", "smk7@cs101-dev-01.cs.illinois.edu", "Shre2909"))
	for server in servers:
		for missing_netid in missing_grades:
			if check_submission(missing_netid, lab, server, passwd):
				submitted_but_not_graded.add(missing_netid)

	for netid in submitted_but_not_graded:
		if netid in missing_grades:
			missing_grades.remove(netid)

	print("-----------Submitted but not graded --------")
	for k in sorted(submitted_but_not_graded):
		print(k)

	print("Not submitted", missing_grades)



if __name__ == "__main__":
	import sys

	section = sys.argv[1]
	lab = sys.argv[2]
	ta_id = sys.argv[3]
	passwd = sys.argv[4]
	combine_grades(section, lab, ta_id, passwd)
