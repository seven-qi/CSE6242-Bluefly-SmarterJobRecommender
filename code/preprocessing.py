from stripHTML import *
import sys

inFilename = sys.argv[1]
#outFilename1 = sys.argv[2]
#outFilename2 = sys.argv[3]

iFile = open(inFilename)
oFile1 = open(outFilename1, 'w')
oFile2 = open(outFilename2, 'w')
count = 0

for line in iFile:
	count +=1 
	l = line.rstrip().split('\t')
	des = l[3]
	req = l[4]
	des = des.replace('\\r', '')
	req = req.replace('\\r', '')
	print des
	# print count
	#oFile1.write(strip_tags(des) + '\n')
	#oFile2.write(strip_tags(req) + '\n')
