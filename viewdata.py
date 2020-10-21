import json
import sys

if len(sys.argv) < 3:
	print("Usage: viewdata.py <data-file> <delimiter> <good/bad/all>")
	exit()

datafile = str(sys.argv[1])
delim = str(sys.argv[2])
opts = str(sys.argv[3])

print(datafile + " " + delim + " " + opts)


print("Records:")

dataFile=open(datafile)

recNum=-1
for rec in dataFile:
	recNum+=1
	if recNum==0:
		cols=list(rec.strip().split(delim))
		cols.insert(0,"rec_num")
		cols.insert(1,"rec_type")
	else:
		vals=list(rec.strip().split(delim))
		vals.insert(0,recNum)
		if len(vals) != len(cols)-1:
			vals.insert(1,"Bad Record")
			badRecDict=dict(zip(cols,vals))
			badRecJson=json.dumps(badRecDict, indent=2)
			if  opts == "bad" or opts == "all":
				print(badRecJson)
		else:
			vals.insert(1,"Good Record")
			goodRecDict=dict(zip(cols,vals))
			goodRecJson=json.dumps(goodRecDict, indent=2)
			if opts == "good" or opts == "all":
				print(goodRecJson)

dataFile.close()