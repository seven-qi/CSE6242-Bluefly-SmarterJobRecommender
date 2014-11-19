import sys

f1 = open(sys.argv[1])

plz = 'Please refer to the Job Description to view the requirements for this job'
for line in f1:
	if plz in line or not line.rstrip():
		pass
	else:
		print line.rstrip()